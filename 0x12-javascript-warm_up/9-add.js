#!/usr/bin/node
const argv = process.argv;

function add (a, b) {
  console.log(a + b);
}
const num1 = Number(argv[2]);
const num2 = Number(argv[3]);

add(num1, num2);
