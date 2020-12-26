var globalEventObj = {}

fetch('http://localhost:8000/calendar/dates').then(function(response){

  return response.json();

 }).then(function(jsondata){

  globalEventObj = jsondata;

 });
