import turtle as t

import random 

tim = t.Turtle()
tim.shape('turtle')
screen = t.Screen()
t.colormode(255)
# color change every step.
def colour_change():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
  



tim.speed('fastest')

def draw_spinograph(size_of_gap):
    for _ in range(int(360 // size_of_gap)):
        tim.color(colour_change())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spinograph(5)

print(tim.heading)
screen.exitonclick()