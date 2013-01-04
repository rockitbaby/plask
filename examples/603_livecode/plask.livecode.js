var vm = require('vm')
  , fs = require('fs')
  , WebSocketServer = require('ws').Server
  , wss = new WebSocketServer({port: 8080})
  , file = ''
  , script = null
  , compiledScript = null
  , drawFunction = null
  , snippetToExecuteNext = null
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

    // in case there is an error, global compiled script is not changed
    compiledScript = precompiledScript;
  } catch(e) {
    // error
    log(e);
  }
}

wss.on('connection', function(ws) {
    /*
    ws.on('message', function(message) {
        compileSnippet(message.code);
    });
    */
});

function compileSnippet(snippet) {
  var sandbox = {};
  vm.runInNewContext(snippet, sandbox);
  if(typeof sandbox.draw == "function") {
    drawFunction = sandbox.draw;
  } else {
    snippetToExecuteNext = snippet;
  }
}

function executeDraw() {
  log = this.setTitle;
  if(drawFunction) {
    drawFunction.apply(this);
  } else if(compiledScript) {
    compiledScript.runInNewContext(this);
  }
  
  if(snippetToExecuteNext) {
    vm.runInNewContext(snippet, this);
    snippetToExecuteNext = null;
  }

}