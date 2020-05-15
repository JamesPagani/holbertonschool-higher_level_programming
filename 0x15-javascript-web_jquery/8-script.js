$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  const movies = data.results;
  $.each(movies, function (index, movie) {
    $('UL#list_movies').append('<li>' + movie.title + '</li>');
  });
});
