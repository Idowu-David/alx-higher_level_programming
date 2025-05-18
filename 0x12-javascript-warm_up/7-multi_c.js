#!/usr/bin/node
const { argv } = require("node:process");

numTimes = Number(argv[2]);
if (numTimes) {
  for (let i = 0; i < numTimes; i++) {
    console.log("C is fun");
  }
} else {
  console.log("Missing number of occurences");
}
