from turtle import Turtle, Screen
import random



# random walk with different colors

colors = [
    "black", "gray", "red", "green", "blue", 
    "yellow", "magenta", "cyan", "brown", "pink", "orange"
]
directions = [0, 90, 180, 270]


tim = Turtle()


tim.shape("turtle")

tim.pensize(15)
tim.speed('fastest')

screen = Screen()
for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(35)
    tim.setheading(random.choice(directions))
               
print(tim.screen)
screen.exitonclick()

