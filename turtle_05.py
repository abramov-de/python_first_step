#!/usr/bin/env python3

import turtle

turtle.shape('turtle')


turtle.color('green')

turtle.begin_fill()
for i in range(1):
    turtle.left(90)
    turtle.forward(50)
for i in range(1):
    turtle.right(90)
    turtle.forward(350)
for i in range(1):
    turtle.right(90)
    turtle.forward(50)
for i in range(1):
    turtle.right(90)
    turtle.forward(350)
turtle.end_fill()



turtle.color('blue')

turtle.begin_fill()
for i in range(1):
    turtle.left(90)
    turtle.forward(50)
for i in range(1):
    turtle.left(90)
    turtle.forward(350)
for i in range(1):
    turtle.left(90)
    turtle.forward(50)
for i in range(1):
    turtle.left(90)
    turtle.forward(350)
turtle.end_fill()


turtle.color('red')

turtle.begin_fill()
for i in range(1):
    turtle.left(90)
    turtle.forward(100)
for i in range(1):
    turtle.left(90)
    turtle.forward(350)
for i in range(1):
    turtle.left(90)
    turtle.forward(50)
for i in range(1):
    turtle.left(90)
    turtle.forward(350)
turtle.end_fill()



turtle.done()
