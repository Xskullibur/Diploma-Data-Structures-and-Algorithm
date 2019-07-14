import turtle


# Draw square based on the size provided
def drawSq(size, myturtle, color):
    myturtle.color("black")
    myturtle.fillcolor(color)
    myturtle.begin_fill()

    for i in range(4):
        myturtle.forward(size)
        myturtle.left(90)

    myturtle.end_fill()


def sierpinski(size, degree, myturtle):

    # Keep calling the method until reaching the smallest degree before starting to draw the squares
    if degree == 0:
        drawSq(size, myturtle, colors[degree])

    else:
        drawSq(size, myturtle, colors[degree])      # Start drawing the base squares while going down the degrees

        # Draw 2 squares and change the direction of the turtle at every loop
        for i in range(4):

            # Draw the first 2 square at the bottom part of the larger square
            sierpinski(size/3, degree-1, myturtle)
            myturtle.forward(size/3)
            sierpinski(size / 3, degree - 1, myturtle)
            myturtle.forward(size / 3)

            # Change the direction of the turtle
            myturtle.forward(size / 3)
            myturtle.left(90)


myTurtle = turtle.Turtle()
myTurtle.shape("turtle")
myTurtle.speed(3)
myTurtle.penup()
myTurtle.goto(-200, -200)
myTurtle.pendown()
myWin = turtle.Screen()

colors = ["blue", "red", "green", "yellow", "orange", "pink", "cyan"]

sierpinski(500, 3, myTurtle)
myWin.exitonclick()