#!/usr/bin/node
/*
A class Rectangle that defines a rectangle:
    You must use the class notation for defining your class
    The constructor must take 2 arguments: w and h
    Initialize the instance attribute width with the value of w
    Initialize the instance attribute height with the value of h
    If w or h is equal to 0 or not a positive integer, create an empty object
    Create an instance method called print() that prints the rectangle using the
         character X
    Create an instance method called rotate() that exchanges the width and the
         height of the rectangle
    Create an instance method called double() that multiples the width and the
         height of the rectangle by 2
*/

class Rectangle {
  constructor (w, h) {
    if (w * h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let ToPrint;
    for (let i = 0; i < this.height; i++) {
      ToPrint = '';
      for (let j = 0; j < this.width; j++) {
        ToPrint += 'X';
      }
      console.log(ToPrint);
    }
  }

  // exchange the width and the height or the Rectangle
  rotate () {
    const aux = this.width;
    this.width = this.height;
    this.height = aux;
  }

  // multiplies width and height of the rectangle by 2
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
