#!/usr/bin/node

const my_filename = process.argv[2];
const fs = require('fs');

fs.readFile(my_filename, 'utf-8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
