#!/usr/bin/node
const argv = process.argv;

const num = Number(argv[2]);

function factorial (n) {
  if (n === 1 || Number.isNaN(n)) {
    return 1;
  }
  return n * factorial(n - 1);
}

console.log(factorial(num));
