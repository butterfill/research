/**
 * (c) 2013 Stephen A. Butterfill
 * 
 */


$(function() {
  // Deck initialization
  $.deck('.slide', {
    fitMode: "center middle",
    designWidth: 800,
    designHeight: 600,
    fitMarginX: 0,
    fitMarginY: 0
  });
});

/**
 * jsPlumb defaults
 */
jsPlumb.Defaults.PaintStyle = {
  lineWidth:2,
  strokeStyle: 'rgba(255,255,0,1)',
  outlineColor: 'black',
  outlineWidth: 1
}
jsPlumb.Defaults.Endpoints = [
  ["Dot", {radius:3}],
  ["Dot", {radius:3}]
]

//- DOESNT WORK
$(document).ready(function(){
  jsPlumb.ready(function(){

    jsPlumb.importDefaults({
      PaintStyle : {
        lineWidth:2,
        strokeStyle: 'rgba(255,255,0,1)',
        outlineColor: 'black',
        outlineWidth: 1
      }
    })
    
  })
})

/**
 * stolen from the deck.scale extension
 * parameter is target height in pixels (e.g. 500)
 */
scaleDeck = function(baseHeight) {
    var opts = $.deck('getOptions');
    var $container = $.deck('getContainer');

    var slideTest = $.map([
        opts.classes.before,
        opts.classes.previous,
        opts.classes.current,
        opts.classes.next,
        opts.classes.after
    ], function(el, i) {
        return '.' + el;
    }).join(', ');

    // Build top level slides array
    var rootSlides = [];
    $.each($.deck('getSlides'), function(i, $el) {
        if (!$el.parentsUntil(opts.selectors.container, slideTest).length) {
            rootSlides.push($el);
        }
    });

    // Scale each slide down if necessary (but don't scale up)
    $.each(rootSlides, function(i, $slide) {
        var slideHeight = $slide.innerHeight(),
        $scaler = $slide
        scale = baseHeight / slideHeight;
        
        $.each('Webkit Moz O ms Khtml'.split(' '), function(i, prefix) {
            if (scale === 1) {
                $scaler.css(prefix + 'Transform', '');
            }
            else {
                $scaler.css(prefix + 'Transform', 'scale(' + scale + ')');
            }
        });
    });
}
