/**
 * deck.velocity.js
 * (c) Stephen A. Butterfill 2014
 * 
 * An extension for deck.js, https://github.com/imakewebthings/deck.js
 * Depends on velocity.js (faster animations)
 * Also depends on jsPlumb if you use +connect
 *
 * I took some ideas from the deck.anim.js plugin.
 *
 * use the associated mixins, e.g.
 *   +animate('.block',{top:150px})
 * becomes:
 *   .dv.dv-velocity(data-what='.block',data-param='{top:150px}')
 *
 * Animations use standard velocity queuing.
 * E.g. the following means the .block element(s) will first move up, then right.
 * (because two animations on the same element occur in sequence).
 * .slide
 *   +animate('.block',{top:150px},{duration:2000})
 *   +animate('.block',{right:150px})
 *
 * Specify queue parameters in the options to create sequential animations.
 * E.g. the following creates diagonal movement:
 * .slide
 *   +animate('.block',{top:150px})
 *   +animate('.block',{right:150px, queue:false})
 *
 * HINT: you may want to use CSS to make sure that action elements like .dv.v-show do not appear.
 */
(function($, deck, undefined) {

  var $d = $(document);
  var slides = [];


  // ------------------------------------------------

  // if you want to add behaviours, just extend the elements_to_actions object.
  // each key is a css class, e.g. dv-velocity 
  // the values are create_doit and create_undoit which return the functions to be run
  // when a slide containing that element becomes current.

  var create_default_undo = function($el, c, action_id) {
    return function(){
      try {
        actions_undo[action_id]();
      } catch(e) {
        // ignore -- sometimes undo called before do in init phase.
      }
    };
  };

  var elements_to_actions = {
    'dv-velocity' : {
      create_doit : function($el, c, action_id) {
        var $targets = c.$targets;
        var css = c.css; 
        if( typeof(css) !== 'object' ) {
          return function(){};
        }
        var options = c.options;
        return function() {
          velocity_create_undo($targets, css, options, action_id);
          $targets.velocity(css,options);
        };
      },
      create_undoit : create_default_undo
    },
    
    'dv-style' : {
      create_doit : function($el, c, action_id) {
        var $targets = c.$targets;
        var css = c.css; 
        if( typeof(css) !== 'object' ) {
          return function(){};
        }
        return function() {
          style_create_undo($targets, css, action_id);
          $targets.css(css);
        };
      },
      create_undoit : create_default_undo
    },
    
    'dv-addclass' : {
      create_doit : function($el, c, action_id) {
        var $targets = c.$targets;
        var cls = c.cls;
        return function(){
          var undo_sequence = [];
          $targets.each(function(idx, target){
            var $target = $(target);
            // careful in making undo -- as some elements may already have the class we're adding,
            // we are going to store the element's currrent classes and restore those later.
            var old_cls = $target.attr('class')  || '';
            log('addclass cls = '+cls+', old_cls ='+ old_cls);
            undo_sequence.push(function(){
              $target.attr('class',old_cls);
            });
            $target.addClass(cls);
          });
          actions_undo[action_id] = function(){
            $.each(undo_sequence, function(_, fn){
              fn();
            });
          };
        };
      },
      create_undoit : create_default_undo
    },
    
    'dv-removeclass' : {
      create_doit : function($el, c, action_id) {
        var $targets = c.$targets;
        var cls = c.cls;
        // re for removing class names matching a pattern like 'highlight-*'
        var to_rm_re;
        if( cls.indexOf('*') !== -1 ) {
          to_rm_re = new RegExp('\\b' + cls.replace(/\*/g,'\\S+').replace(/\s+/g,'|\\b'), 'g');
        }
        return function(){
          // create undo
          var undo_sequence = [];
          log('dv-removeclass nof targets = ' + $targets.length+'; class to remove = '+cls+'; to_rm_re='+to_rm_re);
          $targets.each(function(idx, target){
            var $target = $(target);
            var old_cls = $target.attr('class') || '';
            undo_sequence.push(function(){
              $target.attr('class',old_cls);
            });
          });
          actions_undo[action_id] = function(){
            $.each(undo_sequence, function(_, fn){
              fn();
            });
          };
          // remove classes
          if( !(to_rm_re) ) {
            // class names do not include wildcards (like highlight-*)
            $targets.removeClass(cls);              
          } else {
            // class names include wildcards (like highlight-*)
            $targets.removeClass(function(idx, theClasses){
              var classes_to_remove = (theClasses.match(to_rm_re)||[]).join(' ');
              return classes_to_remove;
            });
          }
          
        };
      },
      create_undoit : create_default_undo
    },
    
    'dv-attr' : {
      create_doit : function($el, c, action_id) {
        var $targets = c.$targets;
        var key = c.attr; //the attribute to modify (e.g. src)
        var value = c.value; //the value to set it to
        return function(){
          var undo_sequence = [];
          $targets.each(function(idx, target){
            var $target = $(target);
            var old_value = $target.attr(key);
            undo_sequence.push(function(){
              $target.attr(key, old_value);
            });
            $target.attr(key,value);
          });
          actions_undo[action_id] = function(){
            $.each(undo_sequence, function(_, fn){
              fn();
            });
          };
        };
      },
      create_undoit : create_default_undo
    },

    'dv-connect' : {
      create_doit : function($el, c, action_id) {
        actions_undo[action_id] = function(){};
        return function(){
          $.deck('disableScale');
          var $top_slide = $el.parents('.slide').last();
          var previous_strokeStyle = jsPlumb.Defaults.PaintStyle.strokeStyle;
          jsPlumb.Defaults.PaintStyle.strokeStyle = c.color;
          jsPlumb.connect({
            source : c.from,
            target : c.to,
            anchors : [c.fromAnchor,c.toAnchor],
            container:  $top_slide
          });
          jsPlumb.Defaults.PaintStyle.strokeStyle = previous_strokeStyle;
          $.deck('enableScale');
        };
      },
      create_undoit : function($el, c, action_id) {
        return function(){
          jsPlumb.detachAllConnections(c.from);
        }
      }
    }
        
  };



  // ------------------------------------------------
  // --- undo ---
  
  // keys are action_ids, values are functions to undo
  // each time you do an action, add an undo function to this object.
  var actions_undo = {};
  
  var css_do_not_undo = ['clipTop','clipRight','clipBottom','clipLeft'];

  function velocity_create_undo($elements, css, options, action_id) {
    var fn_sequence = [];
    var save_clip = css && ('clipTop' in css || 'clipRight' in css || 'clipBottom' in css || 'clipLeft' in css);
    $elements.each(function(idx, el){
      var $el = $(el);
      var old_css = {};
      if( save_clip ) {
        var clip_rect = $el.css('clip');
        fn_sequence.push(function(){
          $el.css('clip', clip_rect);
        });
      }
      
      $.each(css, function(key, val){
        if( $.inArray(key, css_do_not_undo) === -1 ) {
          var old_val = $el.css(key);
          if( typeof(old_val) === 'undefined' ) {
            old_val = $.Velocity.hook($el, key);
          }
          old_css[key] = old_val;
          log('stored for '+action_id+' '+key+':'+old_val);
        }
      });
      var old_options = $.extend({},options);
      old_options.duration = 0;   // because undo
      // original visibility, display needs to be stored if specified
      if( options && 'visibility' in options ) {
        old_options.visibility = $el.css('visibility');
      }
      if( options && 'display' in options ) {
        old_options.display = $el.css('display');
      }
      fn_sequence.push(function(){
        if( !( $.isEmptyObject(old_css) ) ) {
          log('undo velocity action_id='+action_id+' setting these css properties: '+JSON.stringify(old_css)+' with these options: '+JSON.stringify(old_options));
          $el.velocity(old_css, old_options);
        }
      });
    });
    
    actions_undo[action_id] = function(){
      $.each(fn_sequence, function(idx, fn){
        fn();
      });
    };
  }
  
  function style_create_undo($elements, css, action_id) {
    var fn_sequence = [];
    $elements.each(function(idx, el){
      var $el = $(el);
      var old_css = {};
      $.each(css, function(key, val){
        var old_val = $el.css(key);
        old_css[key] = old_val;
        log('style_create_undo stored for '+action_id+' '+key+':'+old_val);
      });
      fn_sequence.push(function(){
        log('undo style action_id='+action_id+' setting these css properties: '+JSON.stringify(old_css)+' on el with class = '+$el.attr('class'));
        $el.velocity('stop');
        setTimeout(function(){
          $el.css(old_css);
        },100);
      });
    });
    
    actions_undo[action_id] = function(){
      $.each(fn_sequence, function(idx, fn){
        fn();
      });
    };
  }
    
  // ------------------------------------------------
  
  function log(msg) {
    // console.log(msg);
  }
  function warn(msg) {
    console.log(msg);
  }

  // ------------------------------------------------
  
  /**
   * converts string like "{a:1}" to an object
   */
  function str_to_obj(str) {
    try {
      return JSON.parse(str);
    } catch(e) {
      // warn('incorrect animation code: '+str);
      return undefined;
    }
  }

  /**
   * $el is like .dv.dv-velocty(data-what='.box', data-css="JSON properties")
   * This function returns an object with the parameters parsed
   */
  function getContext($el) {
    var $top_slide = $el.parents('.slide').last();
    return {
      $targets : $($el.attr('data-what'), $top_slide),
      css : str_to_obj($el.attr('data-css')),
      options : str_to_obj($el.attr('data-options')),
      cls : $el.attr('data-cls') || '',
      attr : $el.attr('data-attr') || '',
      value : $el.attr('data-value') || '',
      // for connect (jsPlumb)
      from: $($el.attr("data-from")),
      fromAnchor:  $el.attr("data-from-anchor") || "RightMiddle",
      to:  $($el.attr("data-to")),
      toAnchor: $el.attr("data-to-anchor") || "RightMiddle",
      color: $el.attr("data-color") || "rgba(255,255,0,1)",
      lineWidth: $el.attr("data-width") || "3",
    };
  }
  


  /**
   * translates an action element into an action object (do and undo functions)
   */
  function getAction($el, action_id) {
    var clss = ($el.attr('class') || '').split(' ');
    log('getAction clss = '+clss);
    var the_action;
    $.each(clss, function(idx, cls){
      if( cls in elements_to_actions ) {
        var actions = elements_to_actions[cls];
        var c = getContext($el);
        the_action = {
          doit : actions.create_doit($el, c, action_id),
          undoit : actions.create_undoit($el, c, action_id)
        };    
      }
    });
    return the_action;
  }
  
  
  /**
   * extracts the elements specifying which actions to perform when
   * $slide becomes current
   */
  function getActions($slide) {
    var $sub_slides = $('.slide', $slide);
    var $sub_slide_actions = $('.dv', $sub_slides);
    var $action_els = $('.dv', $slide).not( $sub_slide_actions );
    var actions = [];
    $action_els.each(function(i, el){
      var $el = $(el);
      var action_id = $slide.attr('id')+'_act-'+i;
      log('action_id: '+action_id);
      var action = getAction($el, action_id);
      if( action ) {
        actions.push( action );
      }
    });
    
    return actions;
  }

  // ------------------------------------------------
  // --- utilities
  
  /**
   * 
   */
  function getSlideIndex($slide){
    if( typeof($slide) === 'undefined' ) {
      $slide = $[deck]('getSlide');
    }
    var idx = 0;
    for( ; idx < slides.length; idx++ ) {
        if( slides[idx].is($slide) ) break;
    }
    return idx;
  } 
  
  /**
   *  force "deck.change" (notification of slide change)
   *  Necessary because can load presentation with e.g. #slide-22
   */
  function forceRefresh() {
    var idx = getSlideIndex();
    $d.trigger("deck.change", [idx, 0]);
    $d.trigger("deck.change", [0, idx]);
  }
  
  // ------------------------------------------------
    
  var doInit = function doInit() {
    
    slides = $[deck]('getSlides');
    log('deck.velocity '+ slides.length);

    log('current slide '+ getSlideIndex());
    
    var velocityEvents = [];
    $.each(slides, function(i, $slide) {
      velocityEvents[i] = getActions($slide);
    });
    
    $(document).bind('deck.change', function(event, from, to) {
      if(to-from === 1) {
        $.each(velocityEvents[to], function(i, action) {
          action.doit();
        });
      } 
      if(to-from > 1) {
        for( var idx = from+1; idx<=to; idx++) {
          $.each(velocityEvents[idx], function(i, action) {
            action.doit();
          });
        }
      }
      if(to-from < 0 ){
        for( var idx = to+1; idx<=from; idx++) {
          var actions = velocityEvents[idx] || [];
          // actions is an array; perform actions undo in reverse order
          for( var idx2 = actions.length-1; idx2 >= 0; idx2 = idx2-1 ) {
            var action = actions[idx2];
            action.undoit();
          }
        }
      }
    });
    
    forceRefresh();
    
  };
  
  $(document).bind('deck.init', function() {
    setTimeout(doInit, 10);
  });
        
})(jQuery, 'deck');

