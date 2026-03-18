from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        # self.color("white")
        self.shape("square")
        self.goto(position)
        self.pos = position

    def move_forward(self):
        self.y_cor = self.ycor() + 20
        self.goto(self.xcor(), self.y_cor)

    def move_backward(self):
        self.y_cor = self.ycor() - 20
        self.goto(self.xcor(), self.y_cor)

    
