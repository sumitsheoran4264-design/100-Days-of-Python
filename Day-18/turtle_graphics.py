#Turtle graphics
from turtle import Turtle, Screen
import random



tim = Turtle()
screen = Screen()


#1. turtle make a dashed line
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# print(tim)
# screen.exitonclick()



# 2. this fuction make 10 different shapes (triangle, squre etc... )
colors = [
    "black", "gray", "red", "green", "blue", 
    "yellow", "magenta", "cyan", "brown", "pink", "orange"
]
def draw_shape(num_sides):
    angle = 360 /  num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shapw_side_n in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shapw_side_n)

print(tim)
screen.exitonclick()




# tim = Turtle()
# screen = Screen()
# tim.shape('turtle')
# tim.color("black", "green")

#3. turtle make a squre
# # for _ in range(4):
# #     tim.forward(100)
# #     tim.right(90)

# print(tim)
# screen.exitonclick()