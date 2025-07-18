import turtle

lebron = ["red", "yellow", "orange", "green", "blue", "purple"]

turtle.bgcolor("white")
turtle.speed(90)

for i in range(360):
    turtle.pencolor(lebron[i % 6])
    turtle.circle(20000)
    turtle.right(59)

turtle.done