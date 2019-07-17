import turtle
import math
from timer import timeit


def calcSmallRadius(radius):
    return radius / (1 + math.sqrt(2))


def drawCicle(radius, myturtle, color):
    myturtle.fillcolor(color)
    myturtle.begin_fill()
    myturtle.circle(radius)
    myturtle.end_fill()

@timeit
def sierpinski(radius, degree, myturtle):

    initalPos = [myturtle.xcor(), myturtle.ycor()]
    drawCicle(radius, myturtle, colors[degree])

    if degree > 0:
        smallRadius = calcSmallRadius(radius)

        myturtle.penup()
        myturtle.left(90)
        myturtle.forward(radius - (smallRadius))
        myturtle.pendown()
        sierpinski(smallRadius, degree - 1, myturtle)

        myturtle.penup()
        myturtle.forward(smallRadius * 2)
        myturtle.pendown()
        sierpinski(smallRadius, degree-1, myturtle)

        myturtle.penup()
        myturtle.right(90)
        myturtle.forward(smallRadius*2)
        myturtle.left(90)
        myturtle.pendown()
        sierpinski(smallRadius, degree - 1, myturtle)

        myturtle.penup()
        myturtle.goto(initalPos[0], initalPos[1])
        myturtle.right(90)


myTurtle = turtle.Turtle()
myTurtle.shape("turtle")
myTurtle.speed(-1)
myTurtle.penup()
myTurtle.goto(0, -300)
myTurtle.pendown()
myWin = turtle.Screen()

colors = ["sky blue", "orange", "green", "yellow", "hot pink", 'blue']

sierpinski(200, 3, myTurtle)
myWin.exitonclick()