from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 22, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0

        with open("data.txt") as file:
            self.highscore = int(file.read())

        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} Highscore: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset_board(self):
        if self.score > self.highscore:
            self.highscore = self.score
        
            with open("data.txt", "w") as file:
                file.write(f"{self.highscore}")

        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg=f"GAME OVER.", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        