#!/bin/bash

latexmk -f lecture*.tex
cp *_handout.pdf ../../../../../raw/index/handout/jekyll/common/assets/pdf/