from turtle import Turtle
FONT = ("Courier", 24, "normal")
class ScoreBoard(Turtle):


    def __init__(self):
        super().__init__()
        self.level = 0
        self.finish = "GAME OVER"
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-212, 255)
        self.write(arg=f"Level:{self.level}", align="center", font=FONT)
        
    
    def increase_score(self):
        self.level += 1
        self.clear()
        self.goto(-212, 255)
        self.write(arg=f"Level:{self.level}", align="center", font=('courier', 30, "normal"))


    def game_over(self):
        self.color("black")
        self.goto(0, 0)
        self.write(arg= self.finish, align="center", font=('courier', 30, "normal"))
        
