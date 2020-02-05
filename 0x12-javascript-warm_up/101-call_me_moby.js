#!/usr/bin/node
/* function that executes x times a function.
     The function must be visible from outside
     Prototype: function (x, theFunction)
     You are not allowed to use var
*/
exports.callMeMoby = function callMeMoby (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
