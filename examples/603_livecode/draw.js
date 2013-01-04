// we are inside the draw function
// edit and save this file, to 'livecode'
var canvas = this.canvas
	, paint = this.paint
	;

// Set the paint to fill an anti-aliased dark red.
paint.setFill();  // Fill is the default, so this is just for clarity.
paint.setAntiAlias(true);
paint.setColor(200, 200, 0, 255);

canvas.clear(230, 230, 230, 255);

var i = 0;
while(i < 40) {
	canvas.drawCircle(paint, i * 30, i % 3 * 50, 30);
	i++;
}