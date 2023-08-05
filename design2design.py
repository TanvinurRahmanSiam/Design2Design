import turtle as t
import colorsys
t.title ('Design2Design')
t.bgcolor("black")
t.tracer(2)
n=1

for i in range(250):
    p = colorsys.hsv_to_rgb(n,0.90, 1)
    n+=0.004
    t.pencolor(p)
    t.left(200)
    t.forward(10-i)
    t.left(150)
    t.circle(50,10)
    t.right(150)
    t.goto(0,0)
    t.forward(250-i)
    t.right(120)
    t.forward(20-i)

t.done()    