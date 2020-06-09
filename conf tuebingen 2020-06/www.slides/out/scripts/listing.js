/**
 * (c) 2013 Stephen A. Butterfill
 * 
 */


$(document).ready(function(){
  $('#sidebar a').each(
    function(){ 
      var menuEntry = $(this).parents('li').first(); 
      var theId = $(this).attr('href'); 
      var theEl = $(theId); 
      theEl.waypoint( function(direction){ 
        var toActivate = menuEntry;
        if(direction=='up'){
          toActivate = menuEntry.prev();
        }
        $('#sidebar .active').removeClass('active');
        toActivate.addClass('active'); 
      }, {offset:100} ); //waypoint options
    }
  ); //each
});
