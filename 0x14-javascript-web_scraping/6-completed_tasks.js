#!/usr/bin/node
/*
script that computes the number of tasks completed by user id.
  The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
  You must use the module request
*/

const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const idArray = [];
    for (let i = 0; i < data.length; i++) {
      if (!(idArray.includes(data[i].userId))) {
        idArray.push(data[i].userId);
      }
    }
    const dictId = {};
    for (let i = 0; i < idArray.length; i++) {
      let count = 0;
      for (let j = 0; j < data.length; j++) {
        if (idArray[i] === data[j].userId) {
          if (data[j].completed) {
            count += 1;
          }
        }
      }
      dictId[i] = count;
    }
    console.log(dictId);
  }
});
