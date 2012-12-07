var vm = require('vm');
var s = 'canvas.drawCircle(paint, 0, 0, 100);';
var script = vm.createScript(s, 'myfile.vm');

//var drawFunction = eval('function(){' + s + '}');

module.exports = function(filename) {
  return function() {
    
    executeDraw.apply(this);
    //eval(s);
  }
}

function executeDraw() {
  
  var canvas = this.canvas, paint = this.paint;console.log("s");
  //canvas.drawCircle(paint, 0, 0, 100);
  //eval(s);
  script.runInThisContext();
  
  //drawFunction.apply(this);
}


