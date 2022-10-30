from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

court = Screen()
court.bgcolor("black")
court.setup(800, 600)
court.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

court.title("PONG!")
court.listen()
court.onkeypress(r_paddle.go_up, "Up")
court.onkeypress(r_paddle.go_down, "Down")
court.onkeypress(l_paddle.go_up, "w")
court.onkeypress(l_paddle.go_down, "s")

game_on = True

place_on_y = 325
for _ in range(15):
    place_on_y -= 50
    place = (0, place_on_y)
    line = Turtle()
    line.shape("square")
    line.shapesize(stretch_wid=1, stretch_len=0.4)
    line.color("white")
    line.pu()
    line.goto(place)

while game_on:
    time.sleep(0.01)
    court.update()
    ball.bounce()

    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.change_direction_ver()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 335 or ball.distance(l_paddle) < 50 and ball.xcor() < -335:
        ball.change_direction_hor()

    if ball.xcor() > 400:
        ball.reset_position()
        ball.x_axis *= -1
        ball.y_axis *= -1
        ball.bounce()
        scoreboard.add_point_left()

    elif ball.xcor() < -400:
        ball.reset_position()
        ball.x_axis *= -1
        ball.y_axis *= -1
        ball.bounce()
        scoreboard.add_point_right()

court.exitonclick()

