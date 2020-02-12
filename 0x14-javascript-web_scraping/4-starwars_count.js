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
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const array = (JSON.parse(body));
    let count = 0;
    const str = 'https://swapi.co/api/people/18/';
    for (let i = 0; i < array.results.length; i++) {
      if (array.results[i].characters.includes(str)) {
        count += 1;
      }
    }
    console.log(count);
  }
});
