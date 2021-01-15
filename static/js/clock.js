var countDownDate = 0;
var event = 0;
fetch('https://gymkhana.ml/event').then(function(response){

  return response.json();

 }).then(function(jsondata){

   countDownDate = new Date(jsondata['dt']).getTime();
   event = jsondata['name']

 });

console.log(countDownDate)
// Update the count down every 1 second
var x = setInterval(function() {

  // Get today's date and time
  var now = new Date().getTime();

  // Find the distance between now and the count down date
  var distance = countDownDate - now;

  // Time calculations for days, hours, minutes and seconds
  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);

  // Display the result in the element with id="demo"
  document.getElementById("eventname").innerHTML = event
  document.getElementById("clock").innerHTML = days + " <font size='6'>Days</font> " + hours + " <font size='6'>Hours</font> "
  + minutes + " <font size='6'>Mins</font> " + seconds + " <font size='6'>Secs</font> ";

  // If the count down is finished, write some text
  if (distance < 0) {
    clearInterval(x);
    document.getElementById("clock").innerHTML = "Countdown Over!";
  }
}, 1000);
