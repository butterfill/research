/*!
Deck JS - deck.remote
for use with chris jaure deckjs-remote thing
-- instead of having his extension just init, this extension tells it to init only if a key 
 is pressed
-- server and port need to be specified!
*/

(function($, deck, undefined) {
  var $d = $(document);
  var $notesContainer;
    
  /*
    Extends defaults/options.
	
      options.keys.notes
		The numeric keycode used to trigger the remote extension setup.
	*/
  $.extend(true, $[deck].defaults, {
    classes: {
      // no classes
    },
    keys: {
      remote: 82 // r
    },
    selectors: {
      // no selector
    }
  });


  /*
   *  jQuery.deck('Init')
   */
  $d.bind('deck.init', function() {
    var opts = $[deck]('getOptions');
    var container = $[deck]('getContainer');
    
    /**
     * how to initialise the deckjs-remote thing
    */
    var init_remote = function(){
      console.log('starting remote')
      $.deck('remote', {
        server: 'http://obscure-stream-2511.herokuapp.com',
        port: 80
        //key: [md5 hash]
       })
    }
    
    var is_master = (window.location.search.search(/[\?&]master([&=]|$)/) != -1);
    var is_client = (window.location.search.search(/[\?&]client([&=]|$)/) != -1);
    if( is_master || is_client ) {
      init_remote();
    }
    // Bind key events 
    $d.unbind('keydown.deckremote').bind('keydown.deckremote', function(e) {
      if (e.which === opts.keys.remote || $.inArray(e.which, opts.keys.remote) > -1) {
        if (e.shiftKey && e.altKey ) {
          init_remote();
          e.preventDefault();
        } 
      }
    });
    
  });
  

})(jQuery, 'deck');