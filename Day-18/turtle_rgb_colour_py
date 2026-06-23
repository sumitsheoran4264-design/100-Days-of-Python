import turtle as t
from turtle import Screen
import random



# color change every step.
def colour_change():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_change = (r, g, b)
    return color_change


directions = [0, 90, 180, 270]


tim = t.Turtle()


tim.shape("turtle")

tim.pensize(15)
tim.speed('fastest')
t.colormode(255)



screen = Screen()
for _ in range(200):
    tim.color(colour_change())
    tim.forward(35)
    tim.setheading(random.choice(directions))
               
print(tim.screen)
screen.exitonclick()

