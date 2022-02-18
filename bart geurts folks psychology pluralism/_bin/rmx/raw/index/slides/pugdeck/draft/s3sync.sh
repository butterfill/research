
#! /bin/bash

# no build needed (already built)

# do not remove any files --- you are writing to the root of slides
# so there are other slides there (maybe)

s3cmd sync out/ s3://philosophical-behavioural-science-slides.butterfill.com --add-header "Cache-Control: max-age=86400"


