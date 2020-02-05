#!/usr/bin/node
/* script that searches the second biggest integer in the list of arguments.
   You can assume all arguments can be converted to integer
   If no argument passed, print 0
   If the number of arguments is 1, print 0
   You must use console.log(...) to print all output
   You are not allowed to use var
*/

if (process.argv[3]) {
  const array = process.argv.slice(2);
  array.sort();
  const num = array.length;
  console.log(array[num - 2]);
} else {
  console.log(0);
}
