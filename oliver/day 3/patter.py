import turtle
bombo = ["red", "orange","yellow", "green", "blue","purple"]


turtle.bgcolor("black")
turtle.speed(0)

for i in range(360):
    turtle.pencolor(bombo[i % 6])
    turtle.forward(i)
    turtle.right(7620)

turtle.done