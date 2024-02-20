#!/usr/bin/node

const ID = process.argv[2];
const URL = `https://swapi.dev/api/films/${ID}/`;
const request = require('request');

let mychars = [];

request.get(URL, (myerror, response, body) => {
  if (myerror) {
    console.log(myerror);
    return;
  }

  const content = JSON.parse(body);
  mychars = content.characters;
  getCharacters(0);
});

const getCharacters = (index) => {
  if (index === mychars.length) {
    return;
  }

  request(mychars[index], (myerror, response, body) => {
    if (myerror) {
      console.log(myerror);
      return;
    }

    const charContent = JSON.parse(body);
    console.log(charContent.name);
    getCharacters(index + 1);
  });
};
