var countDownDate = 0;
var event = 0;
var countDownDatel = 0;
var eventl = 0;
var countDownDater = 0;
var eventr = 0;
fetch('https://activities.kreiva2021.in/event').then(function(response){

  return response.json();

 }).then(function(jsondata){

   countDownDate = new Date(jsondata['dt']).getTime();
   event = jsondata['name'];
   countDownDatel = new Date(jsondata['dtl']).getTime();
   eventl = jsondata['namel'];
   countDownDater = new Date(jsondata['dtr']).getTime();
   eventr = jsondata['namer'];

 }).catch((error) => {

   fetch('https://gymkhana.ml/event').then(function(response){

  return response.json();

 }).then(function(jsondata){

   countDownDate = new Date(jsondata['dt']).getTime();
   event = jsondata['name'];
   countDownDatel = new Date(jsondata['dtl']).getTime();
   eventl = jsondata['namel'];
   countDownDater = new Date(jsondata['dtr']).getTime();
   eventr = jsondata['namer'];

 })

});

function setClock(distance, eventname, suffix)
{
     var days = Math.floor(distance / (1000 * 60 * 60 * 24));
     var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
     var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
     var seconds = Math.floor((distance % (1000 * 60)) / 1000);
     if (distance <= 0) {

       //var myobj = document.getElementById("clock"+suffix);
       //myobj.remove();
       document.getElementById("eventname"+suffix).innerHTML = eventname;
       document.getElementById("days"+suffix).innerText = 0;
       document.getElementById("hours"+suffix).innerText = 0;
       document.getElementById("mins"+suffix).innerText = 0;
       document.getElementById("secs"+suffix).innerText = 0;
       return 0;
     }
     // Display the result in the element with id="demo"
     document.getElementById("eventname"+suffix).innerHTML = eventname;
     document.getElementById("days"+suffix).innerText = days;
     document.getElementById("hours"+suffix).innerText = hours;
     document.getElementById("mins"+suffix).innerText = minutes;
     document.getElementById("secs"+suffix).innerText = seconds;

}
// Update the count down every 1 second
var x = setInterval(function() {

  // Get today's date and time
  var now = new Date().getTime();

  // Find the distance between now and the count down date
  var distance = countDownDate - now;
  var distancel = countDownDatel - now;
  var distancer = countDownDater - now;

  setClock(distance, event, "");
  setClock(distancel, eventl, "l");
  setClock(distancer, eventr, "r");

}, 1000);
