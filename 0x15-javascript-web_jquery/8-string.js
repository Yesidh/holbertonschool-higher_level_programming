/*
Javascript script that fetches and lists all movies title by using this
URL: https://swapi.co/api/films/?format=json
*/
$(function () {
  $.get('https://swapi.co/api/films/?format=json', function (data, textStatus) {
    $.each(data.results, function (list, movie) {
      $('#list_movies').append('<li>' + movie.title + '</li>');
      // $('#list_movies').append($('<li></li>').text(movie.title));
    });
  }, 'json');
});
