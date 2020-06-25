#!/usr/bin/node
const request = require('request');
const movieId = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request.get(movieId, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    characters.forEach((characterURL) => {
      request.get(characterURL, (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
