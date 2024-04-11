from turtle import *
tracer(0)
screensize(100000, 100000)
d = 25
left(90)
pendown()
for _ in range(2):
    forward(d * 13)
    right(90)
    forward(d * 18)
    right(90)
penup()
forward(d * 5)
right(90)
forward(d * 9)
right(90)
pendown()
for _ in range(2):
    forward(d * 11)
    right(90)
    forward(d * 7)
    right(90)
penup()
for x in range(-10, 30):
    for y in range(-10, 30):
        goto(x * d, y * d)
        dot(5, 'red')
update()
done()
