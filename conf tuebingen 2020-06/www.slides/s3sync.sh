#! /bin/bash 

docpad clean

docpad generate --env static

s3cmd sync out/ s3://www.butterfill.com/talk-slides/mindreading_ww/ --add-header "Cache-Control: max-age=86400"
