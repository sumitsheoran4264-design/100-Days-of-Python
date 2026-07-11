from turtle import  Screen
from player import Player
from car_system import Car
from scoreborad import ScoreBoard
import time


#Screen
screen = Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)
screen.title("Go Go Go")

#Player
player = Player()

# scoreboard
scoreboard = ScoreBoard()

# car 
car_manager = Car()
    
#screen listen
screen.onkey(player.move, "Up")

game_on = True

while game_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    if player.ycor() > 290:
        # restet from starting point and increase level 
        player.on_starting_point()
        scoreboard.increase_score()
        car_manager.level_up()  
    

    # detect collison with player
    for car in car_manager.all_cars:
        if car.distance(player) < 22:
            scoreboard.game_over()
            game_on = False

        
    
    




screen.exitonclick()