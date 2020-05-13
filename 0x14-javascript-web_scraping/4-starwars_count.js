#!/usr/bin/node
const request = require('request');
const target = 'https://swapi-api.hbtn.io/api/people/18/';

request.get('https://swapi-api.hbtn.io/api/films/', function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(body).results;
    let appears = 0;
    for (let i = 0; i < JSON.parse(body).count; i++) {
      if (films[i].characters.includes(target)) {
        appears++;
      }
    }
    console.log(appears);
  }
});
