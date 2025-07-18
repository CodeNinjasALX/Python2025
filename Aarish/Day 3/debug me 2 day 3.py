from turtle import *

paddle = Turtle()
paddle.shape("square")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0 -200)
paddle.color("blue")

def move_left():
    x = paddle.xcor() - 20
    paddle.setx(x)

def move_right()
    x = paddle.xcor() + 20
    paddle.setx(x)

screen = Screen()
screen.bgcolor("black")
screen.listen()
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")

done()