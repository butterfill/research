/*!
Deck JS - deck.notes
Copyright (c) 2011 Remi BARRAQUAND
Dual licensed under the MIT license and GPL license.
https://github.com/imakewebthings/deck.js/blob/master/MIT-license.txt
https://github.com/imakewebthings/deck.js/blob/master/GPL-license.txt

MODIFIED by STEVE 2013

TODO: gather findAndReplaceDOMText and apply to notes & handout
*/

/*
This module adds the methods and key binding to show and hide speaker notes.

Create a section for the notes before the .deck-container thus (jade syntax):
	.deck-notes
	  .deck-notes-container

Add notes to slides like this:
  section.slide
    p whatever
    .notes This is a note
    .handout This will appear on the handout

By default, .notes and .handout don't appear on slide.  But if you want them to appear, do:
  p whatever
    .notes.show This is a note that will appear on the slide
    .handout.show This will appear on the handout and on the slide

Using the shift modifier produces a page of notes for export.

Also create a section for the handout export before the .deck-container thus (jade syntax):
	.deck-handout
	  .deck-handout-container

Using the 'h' key produces a handout export page.

To better use this module consider the "deck.clone.js" module which allows to 
clone a deck presentation and displays into a popup window. That way you can
only toggle the notes panel for this cloned window.
*/
(function($, deck, undefined) {
  var $d = $(document);
  var $notesContainer;
    
  /*
    Extends defaults/options.
	
        options.classes.notes
		This class is added to the deck container when showing the slide
                notes.
	
      options.keys.notes
		The numeric keycode used to toggle between showing and hiding 
                the slide notes.
	*/
  $.extend(true, $[deck].defaults, {
    classes: {
      notes: 'deck-notes',
      handout: 'deck-handout',
      notesContainer: 'deck-notes-container',
      handoutContainer: 'deck-handout-container'
    },
    keys: {
      notes: 78, // n
      handout: 72 //h
    },
    selectors: {
      // no selector
    }
  });

  /*
    helper function from https://raw.github.com/padolsey/findAndReplaceDOMText/master/src/findAndReplaceDOMText.js
    license http://unlicense.org/UNLICENSE
  */
  var findAndReplaceDOMText = (function() {

  	var PORTION_MODE_RETAIN = 'retain';
  	var PORTION_MODE_FIRST = 'first';

  	var doc = document;
  	var toString = {}.toString;

  	function isArray(a) {
  		return toString.call(a) == '[object Array]';
  	}

  	function escapeRegExp(s) {
  		return String(s).replace(/([.*+?^=!:${}()|[\]\/\\])/g, '\\$1');
  	}

  	function exposed() {
  		// Try deprecated arg signature first:
  		return deprecated.apply(null, arguments) || findAndReplaceDOMText.apply(null, arguments);
  	}

  	function deprecated(regex, node, replacement, captureGroup, elFilter) {
  		if ((node && !node.nodeType) && arguments.length <= 2) {
  			return false;
  		}
  		var isReplacementFunction = typeof replacement == 'function';

  		if (isReplacementFunction) {
  			replacement = (function(original) {
  				return function(portion, match) {
  					return original(portion.text, match.startIndex);
  				};
  			}(replacement));
  		}

  		// Awkward support for deprecated argument signature (<0.4.0)
  		var instance = findAndReplaceDOMText(node, {

  			find: regex,

  			wrap: isReplacementFunction ? null : replacement,
  			replace: isReplacementFunction ? replacement : '$' + (captureGroup || '&'),

  			prepMatch: function(m, mi) {

  				// Support captureGroup (a deprecated feature)

  				if (!m[0]) throw 'findAndReplaceDOMText cannot handle zero-length matches';

  				if (captureGroup > 0) {
  					var cg = m[captureGroup];
  					m.index += m[0].indexOf(cg);
  					m[0] = cg;
  				}
		 
  				m.endIndex = m.index + m[0].length;
  				m.startIndex = m.index;
  				m.index = mi;

  				return m;
  			},
  			filterElements: elFilter
  		});

  		exposed.revert = function() {
  			return instance.revert();
  		};

  		return true;
  	}

  	/** 
  	 * findAndReplaceDOMText
  	 * 
  	 * Locates matches and replaces with replacementNode
  	 *
  	 * @param {Node} node Element or Text node to search within
  	 * @param {RegExp} options.find The regular expression to match
  	 * @param {String|Element} [options.wrap] A NodeName, or a Node to clone
  	 * @param {String|Function} [options.replace='$&'] What to replace each match with
  	 * @param {Function} [options.filterElements] A Function to be called to check whether to
  	 *	process an element. (returning true = process element,
  	 *	returning false = avoid element)
  	 */
  	function findAndReplaceDOMText(node, options) {
  		return new Finder(node, options);
  	}

  	exposed.Finder = Finder;

  	/**
  	 * Finder -- encapsulates logic to find and replace.
  	 */
  	function Finder(node, options) {

  		options.portionMode = options.portionMode || PORTION_MODE_RETAIN;

  		this.node = node;
  		this.options = options;

  		// ENable match-preparation method to be passed as option:
  		this.prepMatch = options.prepMatch || this.prepMatch;

  		this.reverts = [];

  		this.matches = this.search();

  		if (this.matches.length) {
  			this.processMatches();
  		}

  	}

  	Finder.prototype = {

  		/**
  		 * Searches for all matches that comply with the instance's 'match' option
  		 */
  		search: function() {

  			var match;
  			var matchIndex = 0;
  			var regex = this.options.find;
  			var text = this.getAggregateText();
  			var matches = [];

  			regex = typeof regex === 'string' ? RegExp(escapeRegExp(regex), 'g') : regex;

  			if (regex.global) {
  				while (match = regex.exec(text)) {
  					matches.push(this.prepMatch(match, matchIndex++));
  				}
  			} else {
  				if (match = text.match(regex)) {
  					matches.push(this.prepMatch(match, 0));
  				}
  			}

  			return matches;

  		},

  		/**
  		 * Prepares a single match with useful meta info:
  		 */
  		prepMatch: function(match, matchIndex) {

  			if (!match[0]) {
  				throw new Error('findAndReplaceDOMText cannot handle zero-length matches');
  			}
	 
  			match.endIndex = match.index + match[0].length;
  			match.startIndex = match.index;
  			match.index = matchIndex;

  			return match;
  		},

  		/**
  		 * Gets aggregate text within subject node
  		 */
  		getAggregateText: function() {

  			var elementFilter = this.options.filterElements;

  			return getText(this.node);

  			/**
  			 * Gets aggregate text of a node without resorting
  			 * to broken innerText/textContent
  			 */
  			function getText(node) {

  				if (node.nodeType === 3) {
  					return node.data;
  				}

  				if (elementFilter && !elementFilter(node)) {
  					return '';
  				}

  				var txt = '';

  				if (node = node.firstChild) do {
  					txt += getText(node);
  				} while (node = node.nextSibling);

  				return txt;

  			}

  		},

  		/** 
  		 * Steps through the target node, looking for matches, and
  		 * calling replaceFn when a match is found.
  		 */
  		processMatches: function() {

  			var matches = this.matches;
  			var node = this.node;
  			var elementFilter = this.options.filterElements;

  			var startPortion,
  				endPortion,
  				innerPortions = [],
  				curNode = node,
  				match = matches.shift(),
  				atIndex = 0, // i.e. nodeAtIndex
  				matchIndex = 0,
  				portionIndex = 0,
  				doAvoidNode;

  			out: while (true) {

  				if (curNode.nodeType === 3) {

  					if (!endPortion && curNode.length + atIndex >= match.endIndex) {

  						// We've found the ending
  						endPortion = {
  							node: curNode,
  							index: portionIndex++,
  							text: curNode.data.substring(match.startIndex - atIndex, match.endIndex - atIndex),
  							indexInMatch: atIndex - match.startIndex,
  							indexInNode: match.startIndex - atIndex, // always zero for end-portions
  							endIndexInNode: match.endIndex - atIndex,
  							isEnd: true
  						};

  					} else if (startPortion) {
  						// Intersecting node
  						innerPortions.push({
  							node: curNode,
  							index: portionIndex++,
  							text: curNode.data,
  							indexInMatch: atIndex - match.startIndex,
  							indexInNode: 0 // always zero for inner-portions
  						});
  					}

  					if (!startPortion && curNode.length + atIndex > match.startIndex) {
  						// We've found the match start
  						startPortion = {
  							node: curNode,
  							index: portionIndex++,
  							indexInMatch: 0,
  							indexInNode: match.startIndex - atIndex,
  							endIndexInNode: match.endIndex - atIndex,
  							text: curNode.data.substring(match.startIndex - atIndex, match.endIndex - atIndex)
  						};
  					}

  					atIndex += curNode.data.length;

  				}

  				doAvoidNode = curNode.nodeType === 1 && elementFilter && !elementFilter(curNode);

  				if (startPortion && endPortion) {

  					curNode = this.replaceMatch(match, startPortion, innerPortions, endPortion);

  					// processMatches has to return the node that replaced the endNode
  					// and then we step back so we can continue from the end of the 
  					// match:

  					atIndex -= (endPortion.node.data.length - endPortion.endIndexInNode);

  					startPortion = null;
  					endPortion = null;
  					innerPortions = [];
  					match = matches.shift();
  					portionIndex = 0;
  					matchIndex++;

  					if (!match) {
  						break; // no more matches
  					}

  				} else if (
  					!doAvoidNode &&
  					(curNode.firstChild || curNode.nextSibling)
  				) {
  					// Move down or forward:
  					curNode = curNode.firstChild || curNode.nextSibling;
  					continue;
  				}

  				// Move forward or up:
  				while (true) {
  					if (curNode.nextSibling) {
  						curNode = curNode.nextSibling;
  						break;
  					} else if (curNode.parentNode !== node) {
  						curNode = curNode.parentNode;
  					} else {
  						break out;
  					}
  				}

  			}

  		},

  		/**
  		 * Reverts ... TODO
  		 */
  		revert: function() {
  			// Reversion occurs backwards so as to avoid nodes subsequently
  			// replaced during the matching phase (a forward process):
  			for (var l = this.reverts.length; l--;) {
  				this.reverts[l]();
  			}
  			this.reverts = [];
  		},

  		prepareReplacementString: function(string, portion, match, matchIndex) {
  			var portionMode = this.options.portionMode;
  			if (
  				portionMode === PORTION_MODE_FIRST &&
  				portion.indexInMatch > 0
  			) {
  				return '';
  			}
  			string = string.replace(/\$(\d+|&|`|')/g, function($0, t) {
  				var replacement;
  				switch(t) {
  					case '&':
  						replacement = match[0];
  						break;
  					case '`':
  						replacement = match.input.substring(0, match.startIndex);
  						break;
  					case '\'':
  						replacement = match.input.substring(match.endIndex);
  						break;
  					default:
  						replacement = match[+t];
  				}
  				return replacement;
  			});

  			if (portionMode === PORTION_MODE_FIRST) {
  				return string;
  			}

  			if (portion.isEnd) {
  				return string.substring(portion.indexInMatch);
  			}

  			return string.substring(portion.indexInMatch, portion.indexInMatch + portion.text.length);
  		},

  		getPortionReplacementNode: function(portion, match, matchIndex) {

  			var replacement = this.options.replace || '$&';
  			var wrapper = this.options.wrap;

  			if (wrapper && wrapper.nodeType) {
  				// Wrapper has been provided as a stencil-node for us to clone:
  				var clone = doc.createElement('div');
  				clone.innerHTML = wrapper.outerHTML || new XMLSerializer().serializeToString(wrapper);
  				wrapper = clone.firstChild;
  			}

  			if (typeof replacement == 'function') {
  				replacement = replacement(portion, match, matchIndex);
  				if (replacement && replacement.nodeType) {
  					return replacement;
  				}
  				return doc.createTextNode(String(replacement));
  			}

  			var el = typeof wrapper == 'string' ? doc.createElement(wrapper) : wrapper;

  			replacement = doc.createTextNode(
  				this.prepareReplacementString(
  					replacement, portion, match, matchIndex
  				)
  			);

  			if (!el) {
  				return replacement;
  			}

  			el.appendChild(replacement);

  			return el;
  		},

  		replaceMatch: function(match, startPortion, innerPortions, endPortion) {

  			var matchStartNode = startPortion.node;
  			var matchEndNode = endPortion.node;

  			var preceedingTextNode;
  			var followingTextNode;

  			if (matchStartNode === matchEndNode) {

  				var node = matchStartNode;

  				if (startPortion.indexInNode > 0) {
  					// Add `before` text node (before the match)
  					preceedingTextNode = doc.createTextNode(node.data.substring(0, startPortion.indexInNode));
  					node.parentNode.insertBefore(preceedingTextNode, node);
  				}

  				// Create the replacement node:
  				var newNode = this.getPortionReplacementNode(
  					endPortion,
  					match
  				);

  				node.parentNode.insertBefore(newNode, node);

  				if (endPortion.endIndexInNode < node.length) { // ?????
  					// Add `after` text node (after the match)
  					followingTextNode = doc.createTextNode(node.data.substring(endPortion.endIndexInNode));
  					node.parentNode.insertBefore(followingTextNode, node);
  				}

  				node.parentNode.removeChild(node);

  				this.reverts.push(function() {
  					if (preceedingTextNode === newNode.previousSibling) {
  						preceedingTextNode.parentNode.removeChild(preceedingTextNode);
  					}
  					if (followingTextNode === newNode.nextSibling) {
  						followingTextNode.parentNode.removeChild(followingTextNode);
  					}
  					newNode.parentNode.replaceChild(node, newNode);
  				});

  				return newNode;

  			} else {
  				// Replace matchStartNode -> [innerMatchNodes...] -> matchEndNode (in that order)


  				preceedingTextNode = doc.createTextNode(
  					matchStartNode.data.substring(0, startPortion.indexInNode)
  				);

  				followingTextNode = doc.createTextNode(
  					matchEndNode.data.substring(endPortion.endIndexInNode)
  				);

  				var firstNode = this.getPortionReplacementNode(
  					startPortion,
  					match
  				);

  				var innerNodes = [];

  				for (var i = 0, l = innerPortions.length; i < l; ++i) {
  					var portion = innerPortions[i];
  					var innerNode = this.getPortionReplacementNode(
  						portion,
  						match
  					);
  					portion.node.parentNode.replaceChild(innerNode, portion.node);
  					this.reverts.push((function(portion, innerNode) {
  						return function() {
  							innerNode.parentNode.replaceChild(portion.node, innerNode);
  						};
  					}(portion, innerNode)));
  					innerNodes.push(innerNode);
  				}

  				var lastNode = this.getPortionReplacementNode(
  					endPortion,
  					match
  				);

  				matchStartNode.parentNode.insertBefore(preceedingTextNode, matchStartNode);
  				matchStartNode.parentNode.insertBefore(firstNode, matchStartNode);
  				matchStartNode.parentNode.removeChild(matchStartNode);

  				matchEndNode.parentNode.insertBefore(lastNode, matchEndNode);
  				matchEndNode.parentNode.insertBefore(followingTextNode, matchEndNode);
  				matchEndNode.parentNode.removeChild(matchEndNode);

  				this.reverts.push(function() {
  					preceedingTextNode.parentNode.removeChild(preceedingTextNode);
  					firstNode.parentNode.replaceChild(matchStartNode, firstNode);
  					followingTextNode.parentNode.removeChild(followingTextNode);
  					lastNode.parentNode.replaceChild(matchEndNode, lastNode);
  				});

  				return lastNode;
  			}
  		}

  	};

  	return exposed;

  }());




  /*
    jQuery.deck('showNotes')
    
    Shows the slide notes by adding the class specified by the toc class option
    to the deck container.
	*/
  $[deck]('extend', 'showNotes', function() {
    $notesEl = $("."+$[deck]('getOptions').classes.notes);
    $notesEl.show();
    $('.notes-header-tex', $notesEl).hide();
    if( $notesEl.hasClass('large-format')) {
      $('.deck-container').css({transform:'translate(300px,-200px) scale(0.5,0.5)'});
    } else {
      $('.deck-container').css({transform:'translate(150px)'});
    }
  });
    
  $[deck]('extend', 'showNotesExport', function() {
    $notesEl = $("."+$[deck]('getOptions').classes.notes);
		$notesEl.show();
		$notesEl.addClass('notes-export');
		//show all notes
		$('.notes', $notesEl).show();
		$('.notes-header-tex', $notesEl).show();
		$('.notes-header', $notesEl).hide();
		//$('.divider, .notes-header', $notesEl).show();
		//hide the slides completely
		$('.deck-container').hide();
  });

  $[deck]('extend', 'showHandoutExport', function() {
    $handoutEl = $("."+$[deck]('getOptions').classes.handout);
    $handoutEl.show();
    //hide the slides completely
    $('.deck-container').hide();
  });

  /*
    jQuery.deck('hideNotes')
    
    Hides the slide notes by removing the class specified by the toc class
    option from the deck container.
	*/
  $[deck]('extend', 'hideNotes', function() {
    $("."+$[deck]('getOptions').classes.notes).hide();
    $('.deck-container').css({transform:'translate(0)'});
  });

  $[deck]('extend', 'hideNotesExport', function() {
    $notesEl = $("."+$[deck]('getOptions').classes.notes);
    $notesEl.hide();
    $notesEl.removeClass('notes-export');
    $('.deck-container').show();
  });

  $[deck]('extend', 'hideHandoutExport', function() {
    $handoutEl = $("."+$[deck]('getOptions').classes.handout);
    $handoutEl.hide();
    $('.deck-container').show();
  });
  /*
    jQuery.deck('toggleNotes')
    
    Toggles between showing and hiding the notes.
	*/
  $[deck]('extend', 'toggleNotes', function() {
    $("."+$[deck]('getOptions').classes.notes).is(":visible") ? $[deck]('hideNotes') : $[deck]('showNotes');
  });

	$[deck]('extend', 'toggleNotesExport', function() {
    $("."+$[deck]('getOptions').classes.notes).hasClass("notes-export") ? $[deck]('hideNotesExport') : $[deck]('showNotesExport');
  });

	$[deck]('extend', 'toggleHandoutExport', function() {
    $("."+$[deck]('getOptions').classes.handout).is(":visible") ? $[deck]('hideHandoutExport') : $[deck]('showHandoutExport');
  });


  /*
   *  jQuery.deck('Init')
   */
  $d.bind('deck.init', function() {
    var opts = $[deck]('getOptions');
    var container = $[deck]('getContainer');
    
    // notes can be specified in the url
    var show_notes = (window.location.search.search(/[\?&]notes([&=]|$)/) != -1);
    var large_notes = (window.location.search.search(/[\?&]largenotes([&=]|$)/) != -1);
    if( large_notes ) {
      $notesEl = $("."+$[deck]('getOptions').classes.notes);
      $notesEl.toggleClass('large-format');
    }
    if( show_notes || large_notes) {
      $[deck]('toggleNotes');
    }
    
    // Bind key events 
    $d.unbind('keydown.decknotes').bind('keydown.decknotes', function(e) {
      if (e.which === opts.keys.notes || $.inArray(e.which, opts.keys.notes) > -1) {
        if (e.altKey) {
          $notesEl = $("."+$[deck]('getOptions').classes.notes);
          $notesEl.toggleClass('large-format');
        }
        if (e.shiftKey) {
          $[deck]('toggleNotesExport');
        } else {
          $[deck]('toggleNotes');
        }
        e.preventDefault();
      }
      if (e.which === opts.keys.handout || $.inArray(e.which, opts.keys.handout) > -1) {
        $[deck]('toggleHandoutExport');
        e.preventDefault();
      }
    });
  
		// copy the notes into the special notes element 
		var $notesContainer = $("."+$[deck]('getOptions').classes.notesContainer);
		var $notes = $('.deck-container .notes');
		var slide_id,
			last_slide_id = -1;
		$notes.each( function(idx, note){
			var $note = $(note);

			// usual case -- note belongs to slide which is its parent
			var $slide = $note.parents('.slide').first();

			// but occasionally we want to assign note to a prior sibling (because of the way we use anim and mixins)
			var previous = $note.siblings().splice(0,$note.index());
			var $previous_slide = $(previous).filter('.slide').last();
			if( $previous_slide.length > 0 ) {
				$slide = $previous_slide;
			}

			slide_id = $slide.attr('id');
			if( last_slide_id != -1 && last_slide_id != slide_id ) {
				$notesContainer.append('<div class="divider for-'+last_slide_id+'">--------</div>')
			}
			if( last_slide_id != -1 && last_slide_id != slide_id ) {
				// $notesContainer.append('<div class="notes-header for-'+slide_id+'">Notes for '+slide_id+':</div>');
				// $notesContainer.append('<div class="notes-header-tex for-'+slide_id+'">&nbsp;</div>');
				// $notesContainer.append('<div class="notes-header-tex for-'+slide_id+'">&nbsp;</div>');
				//tex requires that we esacpe _ characters
				var tex_slide_id = (slide_id+'').replace(/_/g,'\\_');
				$notesContainer.append('<div class="notes-header-tex for-'+slide_id+'">\\subsection{'+tex_slide_id+'}</div>');
			}
			//insert note preserving classes
			var cls = $note.attr('class') + (" for-"+slide_id);
			$notesContainer.append('<div class="'+cls+'">'+$note.html().trim()+'</div>');
			// add in a blank line (for latex paragraph) unless .ctd is present
			if( !$notes.eq(idx+1).hasClass('ctd') ) {
				$notesContainer.append('<div class="notes for-'+slide_id+'">&nbsp;</div>');
			}
			last_slide_id = slide_id;
		});

    // escape & characters for latex
    findAndReplaceDOMText($notesContainer[0], {
      find: /&/g,
      replace: '\\&'
    })

				
		// copy the handout elements into the special handout element 
		var $handoutContainer = $("."+$[deck]('getOptions').classes.handoutContainer);

		// the not('.handout .handout') clause ensures we don't add things twice when .handout is nested in .handout
		// (such nesting can be useful for showing and hiding things)
		var $handouts = $('.deck-container .handout').not('.handout .handout');
		var img_path ='';  //set this to use img that appear in both slideshow and handouts (tricky!)
		$handouts.each( function(idx, handout){
			var $handout = $(handout);
			//is it an image?
			if( $handout.not('img').length > 0 && $handout.not('.img').length > 0 ) {
				//it's not an image
				$handoutContainer.append('<div class="handout">'+$handout.html().trim()+'</div>');
				// add in a blank line (for latex paragraph) unless .ctd is present
				if( !$handouts.eq(idx+1).hasClass('ctd') ) {
					$handoutContainer.append("<div>&nbsp;</div>");
				}
			} else {
				//it's an image
				//var $caption = $handout.next('.caption');
				//var caption_txt = $caption.length ? $caption.html() : '';
				var file = $handout.attr('src') || $handout.attr('data-src');
				$.each(['\\begin{center}',
						'\\includegraphics[scale=0.3]{'+img_path+file+'}',
						// '\\caption{'+caption_txt+'}',
						'\\end{center}',
						], function(idx,txt){
					$handoutContainer.append("<div>"+txt+"</div>");
				});
			}
		});

    // add exercises to the end of the handout
    var $exercises = $('.deck-container .exercises');
    if( document.title.match(/^Fast/) ) {
      var $exercises = $('.deck-container .exercises_fast');
    }
    if( $exercises.length > 0 ) {
			$handoutContainer.append("<div>\\vfill</div>")
			$handoutContainer.append("<div>\\begin{minipage}{\\columnwidth}</div>")
			$handoutContainer.append("<div>\\section{Exercises}</div>")
			$handoutContainer.append("<div>These exercises will be discussed in seminars the week after this lecture.</div>")
			$handoutContainer.append("<div>The numbers below refer to the numbered exercises in the course textbook, e.g.\\ `1.1' refers to exercise 1.1. on page 39 of the second edition of \\emph{Language, Proof and Logic}.  Exercises marked `*' are optional.</div>")
			$handoutContainer.append("<div>&nbsp;</div>");
			$handoutContainer.append("<div>\\begin{quote}</div>");
      $exercises.each( function(idx, ex) {
        var $ex=$(ex);
				$handoutContainer.append('<div class="handout exercise">'+$ex.html()+'</div>');
				// add in a blank line (for latex paragraph) unless .ctd is present
				if( !$exercises.eq(idx+1).hasClass('ctd') ) {
					$handoutContainer.append("<div>&nbsp;</div>");
				}
      });
			$handoutContainer.append("<div>\\end{quote}</div>");
			$handoutContainer.append("<div>\\end{minipage}</div>")
    }
    
    // escape & characters for latex
    findAndReplaceDOMText($handoutContainer[0], {
      find: /&/g,
      replace: '\\&'
    });
    findAndReplaceDOMText($handoutContainer[0], {
      find: /⫤⊨/g,
      replace: '$\\leftmodels\\models$'
    });
    findAndReplaceDOMText($handoutContainer[0], {
      find: /⫤/g,
      replace: '$\\leftmodels$'
    });
    findAndReplaceDOMText($handoutContainer[0], {
      find: /⊨TT/g,
      replace: '$\\vDash _{TT}$'
    });
    findAndReplaceDOMText($handoutContainer[0], {
      find: /⊨/g,
      replace: '$\\vDash$'
    });
    findAndReplaceDOMText($handoutContainer[0], {
      find: /⊭TT/g,
      replace: '$\\nvDash _{TT}$'
    });
    findAndReplaceDOMText($handoutContainer[0], {
      find: /⊥/g,
      replace: '$\\bot$'
    });
    findAndReplaceDOMText($handoutContainer[0], {
      find: /⊢/g,
      replace: '$\\vdash$'
    });
    findAndReplaceDOMText($handoutContainer[0], {
      find: /⊬/g,
      replace: '$\\nvdash$'
    });
    findAndReplaceDOMText($handoutContainer[0], {
      find: /⊭/g,
      replace: '$\\nvDash$'
    });

		
  });
    
	$d.bind('deck.change', function(e, from, to) {
		//show notes for current slide
    var slideTo = $[deck]('getSlide', to);
		var $notesContainer = $("."+$[deck]('getOptions').classes.notesContainer);
		$('.notes', $notesContainer).hide();
		$('.divider, .notes-header, .notes-header-tex', $notesContainer).hide();
		var slide_id = $(slideTo).attr('id');
		var $notes = $('.for-'+slide_id, $notesContainer).not('.notes-header-tex');
		$notes.show();
    });

})(jQuery, 'deck');