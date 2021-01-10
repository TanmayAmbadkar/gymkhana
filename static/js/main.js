var globalEventObj = {}

fetch('https://gymkhana.ml/calendar/dates').then(function(response){

  return response.json();

 }).then(function(jsondata){

  globalEventObj = jsondata;

 });

var youtube = document.querySelectorAll( ".youtube" );

for (var i = 0; i < youtube.length; i++) {

    var source = "https://img.youtube.com/vi/"+ youtube[i].dataset.embed +"/mqdefault.jpg";
    var image = new Image();
        image.src = source;
	image.alt = youtube[i].dataset.embed;
        image.classList.add("img-fluid")
        image.addEventListener( "load", function() {
            youtube[ i ].appendChild( image );
        }( i ) );

    youtube[i].addEventListener( "click", function() {
        var iframe = document.createElement( "iframe" );

            iframe.setAttribute( "frameborder", "0" );
            iframe.setAttribute( "allowfullscreen", "" );
            iframe.setAttribute( "src", "https://www.youtube.com/embed/"+ this.dataset.embed +"?rel=0&showinfo=0&autoplay=1" );

            this.innerHTML = "";
            this.appendChild( iframe );
    } );

}
