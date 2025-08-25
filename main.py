from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
#learn ball bouncing
#make ball fast its remaining

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
my_ball = Ball()
l_board = Scoreboard((-100,200))
r_board = Scoreboard((100,200))



screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


is_game_on = True
while is_game_on:

    screen.update()
    time.sleep(0.05)
    my_ball.ball_move()

    # detect collision with upper and bottom wall
    if my_ball.ycor() > 280 or my_ball.ycor() < -280:
        my_ball.bounce_y()

    #detect collision with paddle
    if my_ball.distance(r_paddle) < 50 and my_ball.xcor() > 320 or my_ball.distance(l_paddle) < 50 and my_ball.xcor() < -320:

        my_ball.bounce_x()

    # detect a miss of right paddle
    if my_ball.distance(r_paddle) > 50 and my_ball.xcor() > 380:
        my_ball.goto(0,0)
        my_ball.bounce_x()
        l_board.l_board_score()


    #detect a miss of left paddle
    if my_ball.distance(l_paddle) > 50 and my_ball.xcor() < -380:
        my_ball.goto(0, 0)
        my_ball.sleep_move = 0.1
        my_ball.bounce_x()
        r_board.r_board_score()


screen.exitonclick()