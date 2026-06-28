from colur_tupels_list import color_list
import turtle as turtle_module 
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed('fastest')
tim.penup()
tim.hideturtle()
screen = turtle_module.Screen()


tim.setheading(225)
tim.forward(200)
tim.setheading(0)
number_of_dots = 100
for dots_count in range(1, number_of_dots +1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)


    if dots_count % 10 == 0:
        tim.setheading(90) 
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


    
    



print(tim)
screen.exitonclick()
  