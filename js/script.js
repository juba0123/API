$.getJSON( "file.json", function( data ) {
    var items = [];
    $.each( data, function( key, val ) {
      items.push( "<li class='list-group-item' id='" + key + "'>" + val + "</li>" );
    });
    $( "<ul/>", {
        "class": "list-group",
        html: items.join( "" )
      }).appendTo( "body" );
    });
