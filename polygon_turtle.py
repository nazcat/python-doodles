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
