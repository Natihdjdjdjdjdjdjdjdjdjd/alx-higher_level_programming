#!/usr/bin/node

const URL = process.argv[2];
const request = require('request');

request.get(URL, (myerror, response) => {
  if (myerror) {
    console.log(myerror);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
