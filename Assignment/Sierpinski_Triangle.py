import turtle
from timer import timeit


def drawTriangle(points, myturtle, color):
    myturtle.fillcolor(color)
    myturtle.begin_fill()
    myturtle.up()
    myturtle.goto(points[0][0], points[0][1])
    myturtle.down()
    myturtle.goto(points[1][0], points[1][1])
    myturtle.goto(points[2][0], points[2][1])
    myturtle.goto(points[0][0], points[0][1])
    myturtle.end_fill()


def getMid(p1, p2):
    return ( ( p1[0] + p2[0] ) / 2, ( p1[1] + p2[1] ) / 2 )


def sierpinski(points, degree, myTurtle, color):

    drawTriangle(points, myTurtle, color)

    if degree > 0:
        sierpinski([
            points[0],
            getMid(points[0], points[1]),
            getMid(points[0], points[2])
        ], degree-1, myTurtle, colors[degree-1])

        sierpinski([
            points[1],
            getMid(points[0], points[1]),
            getMid(points[1], points[2])
        ], degree-1, myTurtle, colors[degree-1])

        sierpinski([
            points[2],
            getMid(points[2], points[1]),
            getMid(points[0], points[2])
        ], degree-1, myTurtle, colors[degree-1])


@timeit
def main():
    myTurtle = turtle.Turtle()
    myTurtle.shape("turtle")
    myTurtle.speed(-1)
    myWin = turtle.Screen()

    myPoints = [[-200, -50], [0, 200], [200, -50]]
    degree = 5

    sierpinski(myPoints, degree, myTurtle, colors[degree])

    myTurtle.hideturtle()
    myWin.exitonclick()


colors = ["blue", "red", "green", "yellow", "orange", "pink", "cyan"]
main()