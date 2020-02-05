#!/usr/bin/node
/* script that computes and prints a factorial
*/
const parsed = parseInt(process.argv[2]);
if (isNaN(parsed)) {
  console.log(1);
} else {
  console.log(factorial(parsed));
}
function factorial (n) {
  if (n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
