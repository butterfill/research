#! /bin/bash 

ruby --version # just to run script to set up shell

jekyll clean

jekyll build

s3cmd sync _site/ s3://philosophical-behavioral-science-docs.butterfill.com/ --add-header "Cache-Control: max-age=86400"
