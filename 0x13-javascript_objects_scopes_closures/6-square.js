#!/usr/bin/node
class Square extends require('./5-square') {
  charPrint (c) {
    let sqChar = c;
    let sqRow;
    if (c === undefined) {
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
module.exports = Square;
