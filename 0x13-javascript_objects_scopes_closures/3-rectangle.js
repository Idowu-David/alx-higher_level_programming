#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (!Number.isInteger(w) || w <= 0 || !Number.isInteger(h) || h <= 0) { return; }
    this.width = w;
    this.height = h;
  }

  print () {
    let rect = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        rect += 'X';
      }
      if (i < this.height - 1) rect += '\n';
    }
    console.log(rect);
  }
}

module.exports = Rectangle;
