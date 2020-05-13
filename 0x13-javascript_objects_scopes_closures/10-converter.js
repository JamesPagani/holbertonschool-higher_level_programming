#!/usr/bin/node
exports.converter = function (base) {
  return function (num) {
    console.log(num.toString(base));
  };
};
