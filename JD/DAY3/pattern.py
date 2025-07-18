import turtle

ling = ['red', 'orange', 'yellow', 'green','blue','purple']

turtle.bgcolor("black")
turtle.speed(0)

for i in range(360):
    turtle.pencolor(ling[i % 6])
    turtle.forward(i)
    turtle.right(59)

turtle.done()