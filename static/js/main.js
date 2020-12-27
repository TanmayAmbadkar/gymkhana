var globalEventObj = {}

fetch('http://13.126.197.5/calendar/dates').then(function(response){

  return response.json();

 }).then(function(jsondata){

  globalEventObj = jsondata;

 });
