from turtle import *


import time



ball = Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = 0.15

paddle = Turtle()
paddle.shape("square")
paddle.color("blue")
paddle.shapesize(stretch_wid=1,stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

win = Screen()
win.title("solo pong")
win.bgcolor("black")
win.setup(width=600, height=600)
win.tracer(0)

def move_left():
    x = paddle.xcor() - 20
    if x > -250:
        paddle.setx(x)


def move_right():
    x = paddle.xcor() + 20
    if x < 250:
        paddle.setx(x)


win.listen()
win.onkeypress(move_left, "a")
win.onkeypress(move_right, "d")

while True:
    time.sleep(0.0001)
    win.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.xcor() > 298 or ball.xcor() < -290:
        ball.dx *= -1


    if ball.ycor() > 290:
        ball.dy *= -1



    if ball.ycor() < -290:
        print("you lose resetting...")
        ball.goto(0, 0)
        ball.dy *= -1


    if ball.ycor() < -240 and paddle.distance(ball) < 50:
        ball.dy *= -1