function setup() {
  createCanvas(400, 400);
  frameRate(10)
}

function draw() {
  background(0);
  fill('green')
  r=random(50,width/5)
  circle(width/2,height/2,r)
}