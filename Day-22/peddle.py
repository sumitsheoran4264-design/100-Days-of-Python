from turtle import Turtle

class Peddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("blue")
        self.penup()
        self.goto(position)
        self.shapesize(stretch_wid=5,stretch_len=1)
    
    

    def go_up(self):
        x_cor = self.xcor()
        new_y = self.ycor() + 20
        self.goto(x_cor,new_y)

    def go_down(self):
        x_cor = self.xcor()
        new_y = self.ycor() - 20
        self.goto(x_cor,new_y)

