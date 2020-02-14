/*
Javascript script that fetches and lists all movies title by using this
URL: https://swapi.co/api/films/?format=json
*/
$(function () {
  $.get('https://swapi.co/api/films/?format=json', function (data, textStatus) {
    $.each(data.results, function (index, movie) {
      $('#list_movies').append('<li>' + movie.title + '</li>');
    });
  }, 'json');
});
