from turtle import *
import random
colormode(255)
speed('fastest')
penup()
left(225)
forward(300)
right(225)
pendown()
for b in range(10):
    for a in range(10):
        color([random.randint(0,255),random.randint(0,255),random.randint(0,255)])
        dot(15)
        penup()
        forward(50)
        pendown()
    penup()
    backward(500)
    left(90)
    forward(50)
    right(90)
    pendown()
exitonclick()