#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const options = { baseUrl: 'https://swapi-api.hbtn.io/api/films/', url: id };
request.get(options, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const starwarsTitle = JSON.parse(body).title;
    console.log(starwarsTitle);
  }
});
