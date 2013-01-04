// A simple Plask sketch, how to enable live coding
// 
// Plask follows the CommonJS specification for module loading.
var plask = require('plask')
  // load and initialize the livecode plugin for a file called draw.js
  , livecode = require('./plask.livecode')('draw.js')
  ;

plask.simpleWindow({
  init: function() {
    this.framerate(30);
  },
  draw: livecode // plugin the livecode, the code of draw lives in draw.js
});
