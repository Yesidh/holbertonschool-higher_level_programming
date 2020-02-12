#!/usr/bin/node
/*
A script that prints the number of movies where the character
    “Wedge Antilles” is present.
  The first argument is the API URL of the Star wars API:
     http://swapi.co/api/films/
  Wedge Antilles is character ID 18
  You must use the module request
*/

const request = require('request');
const url = process.argv[2];
const fs = require('fs');
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(process.argv[3], body, 'utf8', function (err, data) {
      if (err) {
        console.log(err);
      }
    });
  }
});
