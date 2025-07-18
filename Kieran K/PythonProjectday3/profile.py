import turtle

name = input("What is thy name?")
color = input("What is thy favorite color?")

def draw_profile(name, color):
    print("Function Ran")
    turtle.bgcolor("white")
    turtle.pensize(5)
    turtle.penup()
    turtle.goto(0,120)
    turtle.color(color)
    turtle.pendown()
    turtle.circle(100)

    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.write(" A B C D E F G H I J K L M N O P Q R S T U V W X Y Z now i know ABCs me and " + name + " are happy u see yayyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy!!! ", align="center", font=("Arial", 1, "bold"))
    turtle.done()

draw_profile(name, color)