var globalEventObj = {}

fetch('http://gymkhana.ml/calendar/dates').then(function(response){

  return response.json();

 }).then(function(jsondata){

  globalEventObj = jsondata;

 });
