from turtle import Turtle
STARTING_POINT = (0, -280)
MOVE_DISTANCE = 10

class Player(Turtle):

    def __init__(self):
        #Player 
        super().__init__()
        self.shape("turtle")
        self.color("blue")
        self.penup()
        self.on_starting_point()
        self.setheading(90)    
      
    #Move Player
    def move(self):
        self.forward(MOVE_DISTANCE)

    def on_starting_point(self):
         self.goto(STARTING_POINT)
         self.setheading(90)  

 