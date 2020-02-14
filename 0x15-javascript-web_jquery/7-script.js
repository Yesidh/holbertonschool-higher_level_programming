/*
Javascript script that fetches and replaces the name of this
URL: https://swapi.co/api/people/5/?format=json
*/
$(function () {
  $.get('https://swapi.co/api/people/5/?format=json', function(data, textStatus) {
    $('#character').text(data.name);
  }, 'json');
});
