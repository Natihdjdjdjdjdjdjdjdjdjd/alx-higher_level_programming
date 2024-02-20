#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (myerr, response, body) {
  if (myerr) {
    console.log(myerr);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let x = 0;
    for (const filmIndex in films) {
      const filmChars = films[filmIndex].characters;
      for (const charIndex in filmChars) {
        if (filmChars[charIndex].includes('18')) {
          x++;
        }
      }
    }
    console.log(x);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
