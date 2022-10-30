from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        Turtle.__init__(self)
        self.shape("circle")
        self.color("white")
        self.speed(9)
        self.penup()
        self.x_axis = 2
        self.y_axis = 2

    def bounce(self):
        """Update ball position on the court."""
        self.goto(self.xcor() + self.x_axis, self.ycor() + self.y_axis)

    def change_direction_ver(self):
        """Change vertical move direction to the opposite one."""
        self.y_axis *= -1

    def change_direction_hor(self):
        """Change horizontal move direction to the opposite one."""
        self.x_axis *= -1

    def reset_position(self):
        """Set ball position to the 0,0 and change its move direction."""
        self.goto(0, 0)
        self.change_direction_hor()
