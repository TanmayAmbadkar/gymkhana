var globalEventObj = {}

fetch('https://gymkhana.ml/calendar/dates').then(function(response){

  return response.json();

 }).then(function(jsondata){

  globalEventObj = jsondata;

 });
