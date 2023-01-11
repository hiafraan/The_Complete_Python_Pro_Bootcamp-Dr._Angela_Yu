from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkeypress(paddle_r.go_up, "Up")
screen.onkeypress(paddle_r.go_down, "Down")
screen.onkeypress(paddle_l.go_up, "w")
screen.onkeypress(paddle_l.go_down, "s")

scoreboard = Scoreboard()

game_on = True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with r_paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
