#!/usr/bin/node
const { argv } = require('node:process');
const intValue = parseInt(argv[2]);
console.log(intValue ? `My number: ${intValue}` : 'Not a number');
