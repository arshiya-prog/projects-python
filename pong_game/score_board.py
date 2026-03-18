from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("purple")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 230)
        self.write(self.l_score, align="center", font=("courier", 50, "normal"))
        self.goto(100, 230)
        self.write(self.r_score, align="center", font=("courier", 50, "normal"))

    def r_scores_pt(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()
    
    def l_scores_pt(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()