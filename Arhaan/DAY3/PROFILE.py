import turtle

name = input("what is your name?")
color = input("what is your favorite color?")

def draw_profile(name, color):
    print("Function Ran")
    turtle.bgcolor("white")
    turtle.pensize(5)
    turtle.penup()
    turtle.goto(0, 120)
    turtle.color(color)
    turtle.pendown()
    turtle.circle(100)

    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.write("hello "+ name + "welcome to python camp.", align="center", font=("Arial", 20 ,"bold"))


    turtle.done()



draw_profile(name, color)