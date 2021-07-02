import turtle

wn = turtle.Screen()
naz = turtle.Turtle()

naz.speed(10)
naz.pensize(5)
naz.color("red")
naz.fillcolor("red")

naz.penup()
naz.forward(-190)
naz.left(90)
naz.forward(100)
naz.pendown()

# "I"
naz.right(90)
naz.forward(50)
naz.forward(-25)
naz.right(90)
naz.forward(175)
naz.right(90)
naz.forward(25)
naz.forward(-50)

naz.penup()
naz.left(180)
naz.forward(100)
naz.pendown()

naz.begin_fill()

# Defining a method to draw curve
def curve():
    for i in range(100):
        naz.right(2)
        naz.forward(2)
  
def heart():
    naz.left(140)
    naz.forward(111)
    curve()
    naz.left(120)
    curve()
    naz.forward(111)
  
    naz.end_fill()

# Draw a heart
heart()

naz.end_fill()

naz.penup()
naz.left(140)
naz.forward(140)
naz.left(90)
naz.forward(175)
naz.pendown()

# "U"
naz.left(180)
naz.forward(150)
naz.left(45)
naz.forward(25)
naz.left(45)
naz.forward(50)
naz.left(45)
naz.forward(25)
naz.left(45)
naz.forward(150)

wn.exitonclick()
