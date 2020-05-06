#!/usr/bin/node
function add(a, b) {
  return a + b;
}

const numOne = parseInt(process.argv[2]);
const numTwo = parseInt(process.argv[3]);
const result = add(numOne, numTwo);
console.log(result);
