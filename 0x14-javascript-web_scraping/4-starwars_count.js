#!/usr/bin/node
const request = require('request');
const target = '/api/people/18/';

request.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(0);
  } else {
    const films = JSON.parse(body).results;
    let appears = 0;
    for (let i = 0; i < JSON.parse(body).count; i++) {
      for (let j = 0; j < films[i].characters.length; j++) {
        if (films[i].characters[j].includes(target)) {
          appears++;
          break;
        }
      }
    }
    console.log(appears);
  }
});
