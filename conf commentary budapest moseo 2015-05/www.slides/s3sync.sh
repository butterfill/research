#! /bin/bash

s3cmd sync out/ s3://www.butterfill.com/talk-slides/bupdapest_moseo/ --add-header "Cache-Control: max-age=86400"
