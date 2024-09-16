from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=right_paddle.up, key='Up')
screen.onkey(fun=right_paddle.down, key='Down')

screen.onkey(fun=left_paddle.up, key="w")
screen.onkey(fun=left_paddle.down, key="s")


game_on = True
while game_on:
    screen.update()
    ball.move()

    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.rebound_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.rebound_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.add_lscore()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.add_rscore()

    scoreboard.update_scoreboard()


screen.exitonclick()
