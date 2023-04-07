from turtle import Screen
from ball import Ball
from paddle import Paddle
from score import Score
import time

STARTING_POSITION_RIGHT = (350, 0)
STARTING_POSITION_LEFT = (-350, 0)

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)
ball = Ball()
r_paddle = Paddle(STARTING_POSITION_RIGHT)
l_paddle = Paddle(STARTING_POSITION_LEFT)
score = Score()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
sleep_time = 0.1

while game_is_on:
    time.sleep(sleep_time)
    screen.update()
    if sleep_time < 0:
        sleep_time = 0
    ball.move()
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce()
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_from_paddle()
        sleep_time -= 0.01
    if ball.xcor() >= 400:
        score.score_l()
        ball.bounce_from_paddle()
        ball.move_after_death()
        sleep_time = 0.1
    elif ball.xcor() <= -400:
        score.score_r()
        ball.bounce_from_paddle()
        ball.move_after_death()
        sleep_time = 0.1


screen.exitonclick()


