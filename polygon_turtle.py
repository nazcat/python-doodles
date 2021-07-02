# create a polygon

import turtle

sides = int(input("Enter number of sides"))
length = int(input("Enter the length of each side"))
lcolor = input("Enter color of polygon")
fcolor = input("Enter fill color of polygon")

wn = turtle.Screen()

naz = turtle.Turtle()
naz.color(lcolor)
naz.fillcolor(fcolor)
naz.pensize(5)

naz.begin_fill()

for i in range(sides):
    naz.forward(length)
    naz.left(360/sides)

naz.end_fill()


# create a smiley

import turtle
wn = turtle.Screen()
wn.bgcolor("lightblue")

naz = turtle.Turtle()
naz.color("purple")

# smiley eyes
naz.penup()
naz.forward(50)
naz.pendown()
naz.left(90)
naz.forward(50)
naz.penup()
naz.left(90)
naz.forward(100)
naz.pendown()
naz.left(90)
naz.forward(50)

# smiley mouth
naz.penup()
naz.right(90)
naz.forward(50)
naz.left(90)
naz.forward(50)
naz.pendown()
naz.left(45)
naz.forward(50)
naz.left(45)
naz.forward(130)
naz.left(45)
naz.forward(50)
