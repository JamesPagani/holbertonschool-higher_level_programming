#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let sqChar = c;
    let sqRow;
    if (typeof c === 'undefined') {
      sqChar = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      sqRow = '';
      for (let j = 0; j < this.width; j++) {
        sqRow += sqChar;
      }
      console.log(sqRow);
    }
  }
}

module.exports = Rectangle;
module.exports = Square;
