from turtle import Turtle
ALIGNMENT = "center" #update score()
FONT = ('Arial', 18, 'normal')
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(x=0, y=275)
        self.update_scoreboard()
        self.hideturtle()
    
    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score}",align=ALIGNMENT,font=FONT)
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER",align= ALIGNMENT,font= FONT)
       
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

