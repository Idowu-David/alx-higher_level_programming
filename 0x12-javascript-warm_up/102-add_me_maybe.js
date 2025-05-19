#!/usr/bin/node

function addMeMaybe (number, theFunction) {
  return theFunction(++number);
}

module.exports = { addMeMaybe }