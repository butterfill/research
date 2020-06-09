# The DocPad Configuration File
# It is simply a CoffeeScript Object which is parsed by CSON
docpadConfig = {

  # http://docpad.org/docs/troubleshoot#watching-doesn-t-work-works-only-some-of-the-time-or-i-get-eisdir-errors
  watchOptions: preferredMethods: ['watchFile','watch']

  plugins:
    #this avoids problems with svg which require text elements!
    text:
      matchElementRegexString: 't'
    # either this or syntax below (newer seems to require this)
    raw:
      raw:
        # rsync
        # -r recursive
        # -u skip file if the destination file is newer
        # -l copy any links over as well
        command: ['rsync', '-rul', 'src/raw/', 'out/' ]


    absolutepath:
      # put the url of the site you are uploading to here, including any subdirectories. 
      url: "https://www.butterfill.com/talk-slides/mindreading_ww/"
    cleanurls:
      getRedirectTemplate: (document) ->
        absolutepath = docpadConfig.plugins.absolutepath.url.slice(0, - 1) 
        """
        <!DOCTYPE html>
        <html>
          <head>
            <meta charset="utf-8">
            <title>#{document.get('title') or 'Redirect'}</title>
            <meta http-equiv="REFRESH" content="0;url=#{absolutepath + document.get('url')}">
          </head>
          <body>
            This page has moved. You will be automatically redirected to its new location. If you aren't forwarded to the new page, <a href="#{absolutepath + document.get('url')}">click here</a>.
          </body>
        </html>
        """
        
  renderPasses : 2

  # =================================
  # Template Data
  # These are variables that will be accessible via our templates
  # To access one of these within our templates, refer to the FAQ: https://github.com/bevry/docpad/wiki/FAQ

  templateData:

    # Specify some site properties
    site:
      # The production url of our website
      url: "https://www.butterfill.com/talk-slides/mindreading_ww/"

      # The default title of our website
      title: "Cooperation and Motor Representation"

      # The website description (for SEO)
      description: """
        Slides for a lecture by s.butterfill@warwick.ac.uk
        """

      # The website keywords (for SEO) separated by commas
      keywords: """
        philosophy, psychology, development, action, joint action, mindreading, motor representation, thought
        """


    # -----------------------------
    # Helper Functions

    # Get the prepared site/document title
    # Often we would like to specify particular formatting to our page's title
    # we can apply that formatting here
    getPreparedTitle: ->
      # if we have a document title, then we should use that and suffix the site's title onto it
      if @document.title
        "#{@document.title} | #{@site.title}"
      # if our document does not have it's own title, then we should just use the site's title
      else
        @site.title

    # Get the prepared site/document description
    getPreparedDescription: ->
      # if we have a document description, then we should use that, otherwise use the site's description
      @document.description or @site.description
    
    getURL : () -> @document.weburl or @site.url

    # Get the prepared site/document keywords
    getPreparedKeywords: ->
      # Merge the document keywords with the site keywords
      @site.keywords.concat(@document.keywords or []).join(', ')
  
    get_unit : (unitNum) ->
      d = @getCollection("documents").findAll({url:'/units/'+unitNum+'.html'},[{year:-1,sort_order:1}]).toJSON()
      if d?[0]?
        if @document.units?.indexOf(unitNum) is -1
          @document.units.push(unitNum)
      else
        d = @getCollection("documents").findAll({url:'/units/'+unitNum+'.html'},[{year:-1,sort_order:1}]).toJSON()
      unit = d?[0]
      if not unit?
        console.log(' ')
        console.log('*** missing unit: '+unitNum)
      return unit

  collections:
    lectures: -> @getCollection('documents').findAll({basename:/^(fast)?lecture_/}, [basename:1])
    units: -> @getCollection('documents').findAll({url:/\/units\/unit_/}, [sequence:1])
      
  
      
}

# Export our DocPad Configuration
module.exports = docpadConfig