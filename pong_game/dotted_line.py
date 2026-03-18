from turtle import Turtle

class DottedLine(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, -280)
        self.pendown()
        self.setheading(90)
    
    def create_line(self):
        self.pendown()
        self.forward(20)
        self.penup()
        self.forward(20)