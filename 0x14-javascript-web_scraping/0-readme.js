#!/usr/bin/node

const fs = require('fs');
const nfile = process.argv[2];

fs.readFile(nfile, 'utf-8', function (myerr, data) {
  if (myerr) {
    console.log(myerr);
  } else {
    console.log(data);
  }
});
