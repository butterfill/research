What It Does
============

This is a collection of files for creating slideshow presentations in html.

Status
======

I'm not ready to share this work, it's only here as my personal backup.  But if you
really wanted to try it out you could.  Be warned that it's temperamental. When things go wrong, as they often do, the error messages are hard to decode.  Most likely it won't work at all.


Requirements
============
You are familiar with, or prepared to learn, the basics of a language called [jade](http://jade-lang.com/).
This is a template language that compiles to html.
(You could write html if you preferred, but it's less work to use jade or something like it.)

It helps to understand basic CSS and javascript too.



Getting Started
===============

Install [node](http://nodejs.org/download/); this is a javascript runtime a tiny bit like java.

Install [docpad](https://docpad.org/docs/install) by opening a terminal and typing:

`npm install -g npm; npm install -g docpad`

Now download the files here and put them into a new folder
called `test_presentation` (say).  (To download the files you can use the 'download ZIP' button that's usually somewhere on the right.)

Open a terminal and navigate to `test_presentation`, which is the folder where you put the files.

Type and run this command:

`npm install; npm rebuild`

to check everything you need for this presentation is correctly installed.

Also type and run:

`docpad generate --env static`

to check it works.

If you have no errors, you can type 

`docpad run`

Now open [http://0.0.0.0:9778/](http://0.0.0.0:9778/) in a web browser and you should see some slides.  
What you're looking at are slides on your local machine, not the web.
If you see some slides, it works!

To edit these slides and make them your own, go to the folder called `test_presentation` where you put all the files.  Now navigate into the `src` sub-folder, then into the `documents` sub-sub-folder, and then open the file index.html.jade in a text editor.

The file testing.html.jade, which is also in the `documents` folder, has some examples in it.  You can view the slides defined in this file  by opening [http://0.0.0.0:9778/testing.html](http://0.0.0.0:9778/testing.html) in a web browser.


Examples
========

Here's [a talk](http://www.butterfill.com/talk-slides/presenting_your_research) and the [source files](https://github.com/butterfill/lectures_presenting_your_research) for it.

Here's [a series of lectures](http://origins-of-mind.butterfill.com/) and the [source files](https://github.com/butterfill/lectures_origins_of_mind_warwick_2014_15) for them.



Why Create Slides This Way?
===========================

It's quicker to create and update slide shows this way.  Suppose you want a slide with some centered text in the middle:

```jade
+slide_middle
  p.center This is a message in the middle of a slide.
```

Do the same but with an image as background

```jade
+slide_middle({bkg:'flowers.png'})
  p.center This is a message in the middle of a slide.
```

where `flowers.png` is the name of a file in `src/raw/img`.

Create a slide with a two column layout:

```jade
+slide_rh_white
  +run_across
    p What is this question?
  +left_half
    p One type of answer.
  +right_half
    p Another type of answer.
```

Do the same but use three slides and have the sentences added to the slides in turn:

```jade
+slide_rh_white
  +run_across
    p What is this question?
  .slide
    +left_half
      p One type of answer.
  .slide
    +right_half
      p Another type of answer.
```

Add some notes (which you can view by pressing `n` while looking at the slides, and export for use with a latex template by pressing `N`):

```jade
+slide_rh_white
  +run_across
    p What is this question?
    .notes This issue goes back at least as far as Plato, who said ... Consider two answers.
  .slide
    +left_half
      p One type of answer.
  .slide
    +right_half
      p Another type of answer.
      .notes Text in notes won't be displayed on the slide.
      p.notes.show (Unless you specify that a note should be displayed by appending '.show', as I've done here.)
```

Show and hide different bits of text on successive slides:

```jade
+slide
  p.question What is the Question?
  p
    span.answer1.hide This is the answer!  
    span.answer2.hide Or maybe it isn't.
  p.evidence-for.hide Some evidence points to one answer.
  p.evidence-against.hide But other evidence points to a conflicting answer.
  .slide
    +show('.evidence-for')
  .slide
    +show('.answer1')
  .slide
    +show('.evidence-against')
  .slide
    +show('.answer2')
  .slide
    +fade('.evidence-for, .evidence-against')
```


Display a quote and then, on the next side, apply a nice highlight effect to any part of the text:

```jade
+slide
  p 
    span 'Sometimes it is nice to 
    span.this-matters highlight
    span  text on a slide.'
  .notes On this slide the quote is displayed with no highlighting.
  
  .slide
    +highlight('.this-matters', 'pink')
    .notes The +highlight command creates a slide.  On this slide the text is highlighted.
  
  .slide
    +unhighlight('.this-matters', 'pink')
    .notes It's easy to remove the highlighting.
  
  .slide
    +blur('span:not(.this-matters)')
    .notes We can also create emphasis by blurring things.
```


What Does the Code in the Samples above Mean?
=============================================

Take the first example.  This line:

`p.center This is a message in the middle of a slide.` 

will be translated into this html fragment:

`<p class="center">This is a message in the middle of a slide.</p>` 

As you can see, Jade uses indentation to save typing tags.  This is one reason for using jade.  The other reason is that Jade allows us to use mixins.   Take the other line of the first example above:

`+slide_middle`

Here we call a mixin, `slide_middle`.  This is equivalent to writing:

```jade
section.slide
  .container_12
    .grid_12
      .words
        .middle
```
(`+slide_middle` is defined in the file `unit_mixins.jade` in the `fragments` folder.)

The examples will compile to a html fragment with this kind of form:

```html
<section class="slide">
  <div class="formatting-stuff">
    <p>Text to appear on a slide</p>
    <!-- we can have nested slides -->
    <div class="slide">
      <p>More text to appear on a slide</p>
    </div>
  </div>
</section>
```

The `deck.js` scripts and css turn a series of fragments like this into a slideshow: they ensure that one `<section class="slide">` is displayed at a time, and allow you to control which slide is displayed using the arrow keys.
  
What about animations---for example, showing or hiding elements on slide, or highlighting elements?  Take the line `+blur('.this-matters')`.  This is roughly equivalent to:

`.slide.anim-addclass(data-what=".this-matters",data-class="blur-text")`

in jade, which translates into:

```html
<div class="slide anim-addclass" data-what=".this-matters" data-class="blur-text">
</div>
```

When this slide becomes current, `deck.js` notices that the slide has the `anim-addclass` class and runs some javascript to add the class `blur-text` to any elements on the slide which have the `this-matters` class.  (You can see how it works in the file `deck.anim.js`.  Note that we depend on jQuery being present; the javascript for adding a class is just `$(selector).addClass(class)`.)




What Are the Components?
========================

The files here comprise a [docpad](https://docpad.org/) project containing  [deck.js](https://github.com/imakewebthings/deck.js), a few other javascript and css components and a collection of jade mixins to make writing slides simple.

[docpad](https://docpad.org/) is a static site builder; it takes a bunch of template and source files and makes web pages from them.

[deck.js](https://github.com/imakewebthings/deck.js) is some javascript and css that allows you to make slide show presentations using HTML instead of having to mess with things like powerpoint.



How Do I Change the Title Page?
===============================

Edit the file `docpad.coffee` in a text editor.


How Do I Put My Slideshow Online?
=================================

Because your slideshow is entirely static documents (html plus css and javascript), you can use any web server you like.  

Run `docpad generate --env static` and then upload the files in the `out` directory onto
your web server; you can use whatever method you would normally use to upload a directory of static files.

Note: If you are uploading to a subfolder, be sure to modify `url` immediately under `absolutepath` in the file `docpad.coffee`.




