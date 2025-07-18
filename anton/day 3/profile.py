import turtle

name = input("What is your name big dawg? ")
color = input("What is your favorite color unc? ")

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
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.write("Wassup " + name + ". Welcome to john pork's basement.", align="center", font=("arial", 20, "bold"))

    turtle.done()


draw_profile(name, color)