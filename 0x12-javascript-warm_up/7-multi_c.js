#!/usr/bin/node
const loops = parseInt(process.argv[2]);
if (isNaN(loops)) {
  console.log('Missing number of ocurrences');
} else {
  for (let i = 0; i < loops; i++) {
    console.log('C is fun');
  }
}
