import turtle

lebron = ["red" , "orange" , "yellow" , "green" , "blue" , "purple" , "white"]

turtle.bgcolor("black")
turtle.speed(0)

for i in range(360):
    turtle.pencolor(lebron[i % 7])
    turtle.forward(i)
    turtle.circle(100)
    turtle.penup()
    turtle.goto(50, 36)
    turtle.pendown()
    turtle.circle(500)
    turtle.right(100)

turtle.done()
