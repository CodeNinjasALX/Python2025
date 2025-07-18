import turtle

lebron =['red', 'orange', 'yellow', 'green', 'blue', 'purple']

turtle.bgcolor('black')
turtle.speed(0)
turtle.pensize(1)
for i in range(500):
    turtle.pencolor(lebron[i % 6])
    turtle.forward(i)
    turtle.circle(2)
    turtle.right(59)

turtle.done()