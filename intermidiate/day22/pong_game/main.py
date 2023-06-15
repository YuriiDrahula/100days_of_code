from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")


left_paddle = Paddle(-350, 0)
right_paddle = Paddle(350, 0)
ball = Ball()
score = ScoreBoard()
screen.tracer(0)


screen.listen()
screen.onkey(key="Up", fun=right_paddle.go_up)
screen.onkey(key="Down", fun=right_paddle.go_down)

screen.onkey(key="w", fun=left_paddle.go_up)
screen.onkey(key="s", fun=left_paddle.go_down)


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 325 or ball.distance(left_paddle) < 50 and ball.xcor() < -325:
        ball.bounce_x()

    # Detect right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        ball.move_opposite()
        score.left_point()

    # Detect left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        ball.move_opposite()
        score.right_point()

screen.exitonclick()