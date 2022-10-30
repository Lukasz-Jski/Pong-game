from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, coordinates):
        self.coordinates = coordinates
        Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(coordinates)

    def go_up(self):
        """Move paddle up the y-axis"""
        self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        """Move paddle down the y-axis."""
        self.goto(self.xcor(), self.ycor() - 20)
