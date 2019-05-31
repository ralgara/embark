#!/usr/bin/env python3

from turtle import *

size=400
min=16

def Sierpinski(l,x,y):
    print(f"l:{l}, x:{x}, y:{y}")
    if l > min:                               # Not done yet?
        l = l / 2                             # scale down by 2
        Sierpinski(l, x, y)                   # bottom left triangle
        Sierpinski(l, x + l, y)               # bottom right triangle
        Sierpinski(l, x + l / 2, y + l)       # top triangle
    else:                                     # Done recursing
        goto(x,y); pendown()                  # start at (x,y)
        begin_fill()                          # prepare to fill triangle
        forward(l); left(120)                 # triangle base
        forward(l); left(120)                 # triangle right
        forward(l)                            # triangle left
        end_fill()
        setheading(0)                         # face East
        penup(); goto(x,y)                    # finish at (x,y)

penup()
pencolor("red")
fillcolor("red")
speed('normal')
Sierpinski(size, -size / 2, -size / 2)
done()