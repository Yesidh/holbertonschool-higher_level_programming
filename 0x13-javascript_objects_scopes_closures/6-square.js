#!/usr/bin/node

const square = require('./5-square');

// inherint from Square
class Square extends square {
  constructor (size) {
    super(size, size);
  }

  // method that prints the rectangle using the character c
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let ToPrint;
    for (let i = 0; i < this.height; i++) {
      ToPrint = '';
      for (let j = 0; j < this.width; j++) {
        ToPrint += c;
      }
      console.log(ToPrint);
    }
  }
}

module.exports = Square;
