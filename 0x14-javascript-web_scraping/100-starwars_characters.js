#!/usr/bin/node
/*
script that prints all characters of a Star Wars movie:
  The first argument is the Movie ID - example: 3 = “Return of the Jedi”
  Display one character name by line
  You must use the Star wars API
  You must use the module request
*/

const request = require('request');
const url = 'https://swapi.co/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body).characters;
    for (let i = 0; i < data.length; i++) {
      request(data[i], function (error, response, body) {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
