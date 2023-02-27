from turtle import Turtle, Screen
from player import Player
from ball import Ball
import time
from scoreboard import Scoreboard
Turtle("classic")
screen = Screen()
screen.title("Pong")
screen.setup(width = 800,height=600)
screen.bgcolor("black")
screen.tracer(0)
speed = 1

r_player = Player((350,0))
l_player = Player((-350,0))
scoreboard = Scoreboard()
ball = Ball()
#players.create_player1()
#players.create_player2()

screen.listen()
screen.onkeypress(r_player.up,"Up")
screen.onkeypress(r_player.down,"Down")
screen.onkeypress(l_player.up,"w")
screen.onkeypress(l_player.down,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision with ceiling or floor
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collsion with right paddle
    if ball.xcor() > 320 and ball.distance(r_player) < 50 or  ball.xcor() < -320 and ball.distance(l_player) < 50:

        ball.bounce_x()

    #detect when right paddle misses
    if ball.xcor() > 380:
        ball.ball_reset_position()
        scoreboard.l_goal_score()


    #detect when left paddle misses
    if ball.xcor() < -380:
        ball.ball_reset_position()
        scoreboard.r_goal_score()
screen.exitonclick()