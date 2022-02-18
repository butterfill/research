ds=deepstream('wss://deepstream.butterfill.com:6020')
# window.lecturer = (username, password) ->
#   ds.close()
#   ds.login({username, password})
username = window.location.search.match(/[\?&]u=(\w+)(&|$)/)?[1] or 'userA'
password = window.location.search.match(/[\?&]p=(\w+)(&|$)/)?[1] or 'password'
follow = window.location.search.match(/[\?&]follow=(\w+)(&|$)/)?[1] 
if follow? or username isnt 'userA'
  ds.login {username,password}, (success, data) ->
    console.log "login success #{success}"
    console.log data
    $(document).ready () ->
      url = $('meta[name=url]').attr('content').replace(/^http[s]?:\/\//, '')
      console.log "url #{url}"
      isLecturer = (username is 'steve')
      if isLecturer
        $(document).bind 'deck.change', (event, from, to) ->
          ds.event.emit  "slideChange:#{url}", {username, from, to}
      else
        ds.event.subscribe "slideChange:#{url}", (data) ->
          console.log data
          if data.username is follow
            # if data.from?
            #   $.deck('go', data.from)
            if data.to?
              $.deck('go', data.to)
  # window.ds = ds