var WebSocketServer = require('ws').Server
  , wss = new WebSocketServer({port: 8080});
wss.on('connection', function(ws) {
  console.log("CONN");
    ws.on('message', function(message) {
        console.log('received: %s', message);
        console.log("");
        console.log("-------------- -------------- -------------- ");
        console.log("");
    });
});
wss.on('error', function(e) {
console.log(e);
});