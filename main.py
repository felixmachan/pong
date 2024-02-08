from turtle import Turtle, Screen
from paddle import Paddle
from line import Line
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350,0)
line = Line()
ball = Ball()
screen.listen()
scoreboard = Scoreboard()


screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()


    #detect collision with paddle
    if ball.distance(r_paddle) < 45 and ball.xcor() > 320 or ball.distance(l_paddle)< 50 and ball.xcor()<-320:
        print("made contact")
        ball.bounce_x()




screen.exitonclick()