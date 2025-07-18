import turtle
name = input("What is your name?")
color = input("What is your favorite color?")
def draw_profile(name, color):
    print("function ran")
    turtle.bgcolor("white")
    turtle.pensize(5)
    turtle.penup()
    turtle.goto(0,120)
    turtle.color(color)
    turtle.pendown()
    turtle.circle(100)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.write("hello " + name + ". welcome to python camp.", align="center", font=("arial", 20, "bold"))

    turtle.done()

draw_profile(name, color)