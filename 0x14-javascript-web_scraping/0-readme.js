#!/usr/bin/node
/*
script that reads and prints the content of a file.
  The first argument is the file path
  The content of the file must be read in utf-8
  If an error oc curred during the reading, print the error object
*/

const fs = require('fs');
const filename = process.argv[2];
fs.readFile(filename, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
