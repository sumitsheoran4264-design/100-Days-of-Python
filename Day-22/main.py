from turtle import  Screen
from peddle import Peddle
from ball import Ball
from scoreboard import ScoreBoard
import time
#screen setup
screen = Screen()
screen.bgcolor("black")
screen.title("Ping Pong")
screen.setup(width=800, height=600)
screen.tracer(0)

#peddles (left or right)
r_peddle = Peddle(position=(350, 0))
l_peddle = Peddle(position=(-350, 0))
 
#Pong ball
ball = Ball()

scoreboard = ScoreBoard()


screen.listen()
#right peddle key
screen.onkey(r_peddle.go_up, "Up")
screen.onkey(r_peddle.go_down, "Down") 

#left peddle key
screen.onkey(l_peddle.go_up, "w")
screen.onkey(l_peddle.go_down, "s")



 



game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect the collision with wall and ball bounce
    if ball.ycor() > 280 or ball.ycor() <-280:
        #need to bounce 
        ball.bounce_y()
    #Detect the collision with right peddle
    if ball.distance(r_peddle) < 50 and ball.xcor() > 320 or ball.distance(l_peddle) < 50 and ball.xcor() < -320:
        #need to bounce 
        ball.bounce_x()
    
    # Detect the R peddle missed
    if ball.xcor() > 380 :
        ball.reset_position()
        scoreboard.l_point()
    # Detect the R peddle missed
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
    


screen.exitonclick()    