from turtle import Screen
from dotted_line import DottedLine
from paddle import Paddle
from ball import Ball
import time
from score_board import ScoreBoard

screen = Screen()
screen.tracer(0)
screen.listen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
r_paddle.color("red")
l_paddle.color("blue")

score_board = ScoreBoard()

dotted_line = DottedLine()
for i in range(0, 30):
    dotted_line.create_line()

screen.onkey(r_paddle.move_forward, "Up")
screen.onkey(r_paddle.move_backward, "Down")
screen.onkey(l_paddle.move_forward, "w")
screen.onkey(l_paddle.move_backward, "s")

ball = Ball()
game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move_ball()

    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.y_bounce()
    
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()

    if ball.xcor() >= 350:
        score_board.l_scores_pt()
        ball.reset_ball()
    elif ball.xcor() <= -400:
        score_board.r_scores_pt()
        ball.reset_ball()

screen.exitonclick()