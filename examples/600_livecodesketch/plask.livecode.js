var vm = require('vm')
  , fs = require('fs')
  , file = ''
  , script = null
  , compiledScript = null
  ;

//var drawFunction = eval('function(){' + s + '}');
var log = function() {};
module.exports = function(filename) {
  file = __dirname + '/' + filename;
  fs.watch(file, [], compileScript);
  compileScript();
  return function() {
    executeDraw.apply(this);
  }
}

function compileScript() {
  script = fs.readFileSync(file, 'UTF-8');
  log('');
  try {
    var precompiledScript = vm.createScript(script, 'myfile.vm');
    compiledScript = precompiledScript;
  } catch(e) {
    // error
    log(e);
  }
}

function executeDraw() {
  log = this.setTitle;
  if(compiledScript) {
    compiledScript.runInNewContext(this);
  }
  
}