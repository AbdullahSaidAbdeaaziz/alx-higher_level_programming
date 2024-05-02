#!/usr/bin/node
const { argv } = require('node:process');
let valueInt = parseInt(argv[2]);
if (!valueInt && valueInt !== 0) console.log('Missing number of occurences');
while (valueInt > 0) {
  console.log('C is fun');
  valueInt--;
}
