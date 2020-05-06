#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  let sqRow;
  for (let i = 0; i < size; i++) {
    sqRow = '';
    for (let j = 0; j < size; j++) {
      sqRow += 'X';
    }
    console.log(sqRow);
  }
}
