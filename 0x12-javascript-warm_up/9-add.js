#!/usr/bin/node
/* script that prints the addition of 2 integers
     The first argument is the first integer
     The second argument is the second integer
     You have to define a function with this prototype: function add(a, b)
     You must use console.log(...) to print all output
     You are not allowed to use var
*/
const add = +process.argv[2] + +process.argv[3];
if (process.argv[2] && process.argv[3]) {
  console.log(add);
} else {
  console.log('NaN');
}
