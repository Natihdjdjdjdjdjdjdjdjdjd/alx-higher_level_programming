#!/usr/bin/node

const ID = process.argv[2];
const URL = `https://swapi.dev/api/films/${ID}/`;
const my_request = require('request');

my_request.get(URL, (myerror, response, body) => {
  if (myerror) {
    console.log(myerror);
    return;
  }

  const data = JSON.parse(body);
  const chars = data.characters;

  for (const character of chars) {
    request(character, (myerror, response, body) => {
      if (myerror) {
        console.log(myerror);
        return;
      }

      const datacontent = JSON.parse(body);
      console.log(datacontent.name);
    });
  }
});
