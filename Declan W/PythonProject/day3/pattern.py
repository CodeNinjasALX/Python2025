import turtle

harrytwinkle2929 = ["red", "orange", "yellow", "green", "blue", "purple"]

turtle.bgcolor("black")
turtle.speed(250)

for i in range(360):
    turtle.pencolor(harrytwinkle2929[i % 6])
    turtle.forward(i)
    turtle.right(1000)

turtle.done()
