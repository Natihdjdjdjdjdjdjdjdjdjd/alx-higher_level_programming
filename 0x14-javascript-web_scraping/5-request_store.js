#!/usr/bin/node

const URL = process.argv[2];
const file = process.argv[3];
const fs = require('fs');
const request = require('request');

request(URL, (myerror, response, body) => {
  if (myerror) {
    console.log(myerror);
  } else {
    fs.writeFile(file, body, 'utf-8', (myerror) => {
      if (myerror) {
        console.log(myerror);
      }
    });
  }
});
