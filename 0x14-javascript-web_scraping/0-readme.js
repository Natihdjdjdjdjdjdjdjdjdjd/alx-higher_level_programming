#!/usr/bin/node

const fname = process.argv[2];
const fs = require('fs');

fs.readFile(fname, 'utf-8', (myerror, data) => {
  if (myerror) {
    console.log(error);
  } else {
    console.log(data);
  }
});
