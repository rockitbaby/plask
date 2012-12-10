var plask = require('plask')
  , omgcanvas = require('./omgcanvas/omgcanvas.js')
  , toxi = require('toxiclibsjs')
  , canvas
  , ctx
  ;

// https://github.com/hapticdata/toxiclibsjs/blob/master/examples/PerlinNoise_canvas.html
// -- schnipp
  var TColor = toxi.color.TColor,
      PerlinNoise = toxi.math.noise.PerlinNoise;
  var palette = [
    TColor.newHex('1c0f17'),
    TColor.newHex('271d2e'),
    TColor.newHex('2c3857'),
    TColor.newHex('155e73').setBrightness(0.9),
    TColor.newHex('e8ca59'),
    TColor.newHex('891b1b').setAlpha(0.85),
  ];
  
  var perlin = new PerlinNoise()
    , offset = 0
    , options = {
        numStreams: 500,
        distort: 0,
        strength:  Math.PI,
        scaler: 0.05,
        step: 2
      }
    , streams = []
    ;
  var getRandomVector = function(){
    var vec = new toxi.geom.Vec2D(Math.random() * canvas.width, Math.random() * canvas.height);
    vec.color = palette[parseInt(Math.random() * palette.length, 10)];
    return vec;
  };

plask.simpleWindow({
  settings: {
    type: '3d2d',
    width: 800,
    height: 500
  },
  init: function() {
    this.framerate(30);
    canvas = this.canvas;
    ctx = omgcanvas.CanvasContext(canvas);

    for(var i=0; i < options.numStreams; i++) {
      streams.push(getRandomVector());
    }

    ctx.fillStyle = "#000000";
    ctx.strokeStyle = "#ff0000";
    ctx.lineWidth = 1.5;

  },
  draw: function() {
    this.setTitle(this.framenum);
    var canvas = this.canvas, paint = this.paint;

    //
    while(options.numStreams > streams.length) {
      streams.push(getRandomVector());
    }
    while(options.numStreams < streams.length) {
      streams.shift();
    }
    offset += options.distort;
    ctx.fillStyle = "rgba(0,0,0,0.05)";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    var replaceIndices = [];
    var lastPos = new toxi.geom.Vec2D();

    streams.forEach(function(stream, i) {
      stream.color;
      ctx.strokeStyle = stream.color.toRGBACSS();
      lastPos.set(stream);

      var noise = perlin.noise(stream.x * options.scaler, offset + stream.y * options.scaler) - 0.5;
      var angle = options.strength * noise;
      var dir = toxi.geom.Vec2D.fromTheta(angle);
      
      stream.addSelf(dir.normalizeTo(options.step * 3));
      ctx.beginPath();
      ctx.moveTo(lastPos.x, lastPos.y);
      ctx.lineTo(stream.x, stream.y);
      ctx.closePath();
      ctx.stroke();
      if(stream.x < 0 || stream.x > canvas.width || stream.y < 0 || stream.y > canvas.height) {
        replaceIndices.push(i);
      }
    });

    replaceIndices.forEach(function(streamIndex){
      streams[streamIndex] = getRandomVector();
    });

  }
});
