from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

for i in range(0, 4):
    timmy.forward(100)
    timmy.right(90)

screen.exitonclick()