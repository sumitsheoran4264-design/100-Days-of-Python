from turtle import Turtle
ALIGNMENT = "center" #update score()
FONT = ('Arial', 18, 'normal')
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("Day-24\\data.txt") as data:
           self.high_score = int(data.read())
        self.penup()
        self.color("white")
        self.goto(x=0, y=275)
        self.update_scoreboard()
        self.hideturtle()
    
    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}",align=ALIGNMENT,font=FONT)
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("Day-21\\data.txt",mode= "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
        
    
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER",align= ALIGNMENT,font= FONT)
       
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    
