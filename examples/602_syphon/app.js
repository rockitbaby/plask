var plask = require('plask')
  ;

plask.simpleWindow({
  settings: {
    type: '3d2d',
    syphon_server: 'plask' // name of syphon server, all you need to do to publish to syphon
  },
  init: function() {
    this.framerate(30);

    // see 002_hello_circle_pulse.js, rewritten using with() statement (not sure if I like using with, yet)
    with(this.paint) {
      setFill();
      setAntiAlias(true);
      setColor(80, 0, 0, 255);
    }
  },
  draw: function() {
    this.setTitle(this.framenum);
    var t = Math.sin(this.frametime) * 0.5 + 0.5;
    var radius = plask.lerp(50, 100, t);
    
    with(this) {
      canvas.clear(230, 230, 230, 255);
      canvas.drawCircle(paint, 200, 150, radius);
    }
    
  }
});
