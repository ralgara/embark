#!/usr/bin/env python3

from turtle import *
import pdb
from random import random, seed

def drawSpiral(diameter, angle):
    if diameter > 0:

        t.pencolor(
            0,
            0,
            diameter/size
        )
        """t.pencolor(
            random(),
            random(),
            random()
        )"""

        t.forward(diameter)
        t.left(angle)

        print(locals())

        drawSpiral(
            diameter - 2,
            angle
        )


seed(0)

s = Screen()
s.colormode(1)
size = 500
s.setworldcoordinates(0, 0, size, size)

t = Turtle()
t.width(3)
t.speed(100)

drawSpiral(
    diameter = size/10,
    angle = 21
)

Screen().exitonclick()

#pdb.set_trace()