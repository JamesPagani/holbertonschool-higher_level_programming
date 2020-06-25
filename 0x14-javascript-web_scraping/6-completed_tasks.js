#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const completedTodos = {};
    const todos = JSON.parse(body);
    for (let i = 0; i < todos.length; i++) {
      if (todos[i].completed === true) {
        const id = todos[i].userId;
        if (id in completedTodos) {
          completedTodos[id]++;
        } else {
          completedTodos[id] = 1;
        }
      }
    }
    console.log(completedTodos);
  }
});
