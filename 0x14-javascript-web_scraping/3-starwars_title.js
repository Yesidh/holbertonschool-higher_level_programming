#!/usr/bin/node
/*
A script that prints the title of a Star Wars movie where the episode number
   matches a given integer.
  The first argument is the movie ID
  You must use the Star wars API with the endpoint http://swapi.co/api/films/:id
  You must use the module request
*/

const request = require('request');
const url = 'https://swapi.co/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
