#!/usr/bin/node

const URL = process.argv[2];
const ID = '18';
const request = require('request');

request.get(URL, (myerror, response, body) => {
  if (myerror) {
    console.log(myerror);
  } else {
    let pro = 0;
    const content = JSON.parse(body);

    content.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(ID)) {
          pro += 1;
        }
      });
    });
    console.log(pro);
  }
});
