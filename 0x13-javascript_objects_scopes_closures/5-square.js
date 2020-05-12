#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let sqRow;
    for (let i = 0; i < this.height; i++) {
      sqRow = '';
      for (let j = 0; j < this.width; j++) {
        sqRow += 'X';
      }
      console.log(sqRow);
    }
  }

  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Rectangle;
module.exports = Square;
