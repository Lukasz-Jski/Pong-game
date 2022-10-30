from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        Turtle.__init__(self)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_scoreboard = 0
        self.r_scoreboard = 0
        self.update()

    def update(self):
        """Print actual score for both left and right players."""
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_scoreboard, align="center", font=("Verdana", 70, "normal"))
        self.goto(100, 200)
        self.write(self.r_scoreboard, align="center", font=("Verdana", 70, "normal"))

    def add_point_left(self):
        """Add one point to the player on the left side."""
        self.l_scoreboard += 1
        self.update()

    def add_point_right(self):
        """Add one point to the player on the right side."""
        self.r_scoreboard += 1
        self.update()
