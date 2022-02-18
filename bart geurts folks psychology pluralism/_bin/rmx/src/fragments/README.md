I use these as mixins when creating deck.js slides for lectures or talks using pug.

Include them as a git submodule in the repo for your lectures or slides

They were originally jade mixins. The main difference is that pug removed the neat
interpolation (e.g. "/asd#{pathname}/#{filename}.txt") which needed to be replaced
by `asd ${pathname} dfuo` (fiddly).