1. copy the files in this directory (EXCEPT the .git subfolder) into a new blank directory where you want to create the slides.


2. [NO LONGER NECESSARY] run:

npm install

(this installs the dependencies from package.json)


3. create:

docpad generate --env static


3b. [optional] to update local version docpad and plugins (CAUTION: may not work)

docpad update


3c. You may also get the latest deck.core.js (but don't upgrade deck.core.css)


4. serve

cd out/
serve.sh
(i.e. python -m SimpleHTTPServer 8080)


5. specify path in for absouluteurl plugin in docpad.coffee
  absolutepath:
    url: "/"


6. create s3sync.sh to upload specifying ***SUBDIR***

s3cmd sync out/ s3://www.butterfill.com/talk-slides/*SUBDIR*/ --add-header "Cache-Control: max-age=86400"


7. nb for watching

docpad watch --env static

7b sometimes generates 	EMFILE error, in that case:

ulimit -n 8192

