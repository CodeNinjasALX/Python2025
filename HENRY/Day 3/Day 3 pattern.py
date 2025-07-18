import turtle
list12345 = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle.bgcolor("black")
turtle.pensize(10)
turtle.speed(50)
for i in  range(3600):
    turtle.pencolor(list12345[i % 6])
    turtle.circle(i * 1.1)
    turtle.right(59)
turtle.done()