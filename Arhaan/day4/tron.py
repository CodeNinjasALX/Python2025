import turtle

import freegames
from turtle import *
from freegames import square, vector

p1xy = vector(-100, 0)
p1aim = vector(4, 0)
p1body = set()

p2xy = vector(100, 0)
p2aim = vector(-4, 0)
p2body = set()

def inside(head):
    return -200 <head.x < 200 and -200 < head.y < 200

def draw():
    p1xy.move(p1aim)
    p1head = p1xy.copy()

    p2xy.move(p2aim)
    p2head = p2xy.copy()


    if not inside(p1head) or p1head in p2body or p1head in p1body:
        print('player red wins!')
        return

    if not inside(p2head) or p2head in p1body or p2head in p2body:
        print('player blue wins!')
        return


    p1body.add(p1head)
    p2body.add(p2head)


    square(p1xy.x,p2xy.y, 5, "red")
    square(p2xy.x, p2xy.y, 5, "blue")

    update()
    ontimer(draw, 50)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)

listen()

onkey(lambda: p1aim.__init__ (0,4), "w")
onkey(lambda: p1aim.__init__ (0,-4), "a")
onkey(lambda: p1aim.__init__ (-4,0), "s")
onkey(lambda: p1aim.__init__ (4,0), "d")

onkey(lambda: p2aim.__init__ (0,4),  "i")
onkey(lambda: p2aim.__init__ (0,-4),  "k")
onkey(lambda: p2aim.__init__ (-4,0),  "j")
onkey(lambda: p2aim.__init__ (4,0), "l")

draw()
done()
