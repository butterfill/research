(function() {
  var ds, follow, password, ref, ref1, ref2, username;

  ds = deepstream('wss://deepstream.butterfill.com:6020');

  username = ((ref = window.location.search.match(/[\?&]u=(\w+)(&|$)/)) != null ? ref[1] : void 0) || 'userA';

  password = ((ref1 = window.location.search.match(/[\?&]p=(\w+)(&|$)/)) != null ? ref1[1] : void 0) || 'password';

  follow = (ref2 = window.location.search.match(/[\?&]follow=(\w+)(&|$)/)) != null ? ref2[1] : void 0;

  if ((follow != null) || username !== 'userA') {
    ds.login({
      username: username,
      password: password
    }, function(success, data) {
      console.log("login success " + success);
      console.log(data);
      return $(document).ready(function() {
        var isLecturer, url;
        url = $('meta[name=url]').attr('content').replace(/^http[s]?:\/\//, '');
        console.log("url " + url);
        isLecturer = username === 'steve';
        if (isLecturer) {
          return $(document).bind('deck.change', function(event, from, to) {
            return ds.event.emit("slideChange:" + url, {
              username: username,
              from: from,
              to: to
            });
          });
        } else {
          return ds.event.subscribe("slideChange:" + url, function(data) {
            console.log(data);
            if (data.username === follow) {
              if (data.to != null) {
                return $.deck('go', data.to);
              }
            }
          });
        }
      });
    });
  }

}).call(this);
