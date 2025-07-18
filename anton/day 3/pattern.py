import turtle

lebron = ["green", "black", "white"]

turtle.bgcolor("black")
turtle.speed(150)
turtle.pensize(10)

for i in range(360):
    turtle.pencolor(lebron[i % 3])
    turtle.forward(i * -10 + 19)
    turtle.forward(i * 21 + -2)
 #   turtle.circle(50 + i * 20)
    turtle.circle(40 + -20 + 6 * 3)
    turtle.right(200)


turtle.done()