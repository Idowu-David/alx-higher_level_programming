#!/usr/bin/node
const { argv } = require("node:process");

let max1 = -Infinity;
let max2 = -Infinity;

if (argv.length === 2) {
  console.log(0);
} else if (argv.length === 3) {
  console.log(1);
} else {
  for () {
    if (n > max1) {
      max2 = max1;
      max1 = n;
    } else if (n < max1 && n > max2) {
      max2 = n;
    }
  }
}
return;

/**
 *
 */
