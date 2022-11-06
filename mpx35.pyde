def setup():
    size(600,400)
def draw():
    background(255)
    fill(random(0,255),random(0,255),random(0,255))
    line(300,200,random(0,600),random(0,400))
    translate(200,100)
    noFill()
    ellipse(100,100,500,400)
