/*!
Deck JS - deck.slide-cone
an extension to allow cloning slides.

Doesn't produce predictable results in mildly complicated cases, e.g. slides with subslides
Suggest not using!

Use like this (jade syntax), where the data-which attribute specifies a selector:
section.slide
  .slide-clone(data-which='#dyuia')
  p Other stuff can be appended (or prefixed)

Each .slide-clone will only do one clone using the current state of the slide to be cloned.
  
Copyright (c) 2013 Steve Butterfill
Dual licensed under the MIT license and GPL license.
https://github.com/imakewebthings/deck.js/blob/master/MIT-license.txt
https://github.com/imakewebthings/deck.js/blob/master/GPL-license.txt
*/

/*
Clone a slide when the slide with .slide-clone element in it becomes current,
and do the cloning just once.  This ensures that the slide is cloned in its latest state
(rather than, say, its initial state).
*/
(function($, deck, undefined) {
	
  $('.slide-clone').each(function(i, el) {
    var $el = $(el);
    $el.parents('.slide').first().one('deck.becameCurrent', function(_, direction, from, to) {
      var selector = $el.attr('data-which');
      var $to_clone = $(selector);
      var theClone = $to_clone.clone();
      if( $to_clone.length === 0 ) {
        theClone = $('<p>[*not found, selector='+selector+'*]</p>');
      }
      
      console.log('cloning: found = '+$to_clone.length)

      //sort out subslides by removing the slide class from elements in the clone 
      // (may create complications if slide not yet been fully revealled)
      $(theClone).find('.slide.deck-before').removeClass('slide').removeClass('deck-before');

      //remove notes and handouts from the clone (don't want them duplicated)
      //do this in two steps
      // first step: where notes should appear on the slide, remove notes class
      $(theClone).find('.notes.show').removeClass('notes');
      $(theClone).find('.handout.show').removeClass('handout');
      // second step: where notes are hidden, remove notes altogether
      $(theClone).find('.notes').remove();
      $(theClone).find('.handout').remove();

      //clear out any old content and put the clone into the .slide-clone element
      $el.html(theClone.html());
    });
  });

})(jQuery, 'deck');
