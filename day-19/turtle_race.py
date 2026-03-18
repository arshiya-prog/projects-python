from turtle import Turtle, Screen
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
game_is_on = True

screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput("Make your bet", "Who will win the race? Enter a color: ")
y_positions = [-125, -75, -25, 25, 75, 125]

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_positions[turtle_index])
    turtles.append(new_turtle)

while game_is_on:
    for turtle in turtles:
        if turtle.xcor() >= 230:
            game_is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")

        step = random.randint(0, 10)
        turtle.forward(step)

screen.exitonclick()