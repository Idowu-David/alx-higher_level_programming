#!/usr/bin/node
const { argv } = require("node:process");

myNum = argv[2];
if (myNum === undefined) {
  console.log("Not a number");
} else {
	const n = Number(myNum);
	if (n) {
		console.log('My number: %s', n);
	} else {
		console.log('Not a number');
	}
}
