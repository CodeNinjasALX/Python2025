# DebugMe: Fix this Turtle Shape Drawer

import turtle


def draw_square():
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)


turtle.color = "blue"
draw_square()
turtle.done()

