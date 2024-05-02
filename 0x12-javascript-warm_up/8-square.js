#!/usr/bin/node
const { argv, exit } = require('node:process');

const valueInt = parseInt(argv[2]);

if (!valueInt && valueInt !== 0) { console.log('Missing size'); exit(0); }

let width = valueInt;
while (width > 0) {
  let temp = valueInt;
  while (temp > 0) {
    process.stdout.write('X');
    temp--;
  }
  process.stdout.write('\n');
  width--;
}
