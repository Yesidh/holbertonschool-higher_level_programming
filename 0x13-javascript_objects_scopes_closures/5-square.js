#!/usr/bin/node
const Rectangle = require('./4-rectangle');
/*
A class Square that defines a square and inherits from Rectangle of
    4-rectangle.js:
  You must use the class notation for defining your class and extends
  The constructor must take 1 argument: size
  The constructor of Rectangle must be called (by using super())
*/

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
