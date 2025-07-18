import turtle

name = input("whats your name")
color = input("whats your favorite color")

def draw_profile(name, color):
    print("function ran")
    turtle.bgcolor("white")
    turtle.pensize(5)
    turtle.penup()
    turtle.goto(-40, 120)
    turtle.color(color)
    turtle.pendown()
    turtle.circle(-1111)

    turtle.penup()
    turtle.goto(-33, 0)
    turtle.pendown()
    turtle.write("i kill good domnom" + name + ". welcome to the oboma.", align="center", font=("cursive", 10, "bold"))



    turtle.done()

draw_profile(name, color)