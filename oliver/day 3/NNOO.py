import turtle
import colorsys
import math
import time

screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.tracer(0, 0)

t = turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()
screen.colormode(1.0)

num_spirals = 6
points_per_spiral = 120
max_radius = 250

def draw_spiral(turt, base_angle, pulse, direction=1):
    for i in range(points_per_spiral):
        angle = (i * 10 * direction) + base_angle
        radius = max_radius * (i / points_per_spiral) * (0.7 + 0.3 * math.sin(pulse * 5 + i))
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        hue = ((i / points_per_spiral) + pulse) % 1.0
        r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
        turt.pencolor(r, g, b)
        if i == 0:
            turt.penup()
            turt.goto(x, y)
            turt.pendown()
        else:
            turt.goto(x, y)

def draw_kaleidoscope(frame):
    t.clear()
    pulse = frame * 0.03
    base_angle = frame * 3
    for i in range(num_spirals):
        angle_offset = (360 / num_spirals) * i
        direction = 1 if i % 2 == 0 else -1
        draw_spiral(t, base_angle + angle_offset, pulse, direction)
    screen.update()

frame = 0
try:
    while True:
        draw_kaleidoscope(frame)
        frame += 1
        time.sleep(0.02)
except turtle.Terminator:
    pass
