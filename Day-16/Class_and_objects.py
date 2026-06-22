# import turtle
# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("yellow", "black")
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

#Table 
from prettytable import PrettyTable

table = PrettyTable()


table.add_column("Pokemon", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electirc", "Water", "Fire"])
table.align = "l"
print(table)  