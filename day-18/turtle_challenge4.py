import turtle as t
import random as rd

tim = t.Turtle()
screen = t.Screen()

t.colormode(255)

tim.speed(0)
tim.pensize(10)
tim.hideturtle()

def random_color():
    r = rd.randint(0, 255)
    g = rd.randint(0, 255)
    b = rd.randint(0, 255)
    return (r, g, b)

moves = [
    lambda: tim.forward(20), 
    lambda: tim.right(90), 
    lambda: tim.left(90), 
    lambda: tim.left(180)
]

for _ in range(200):
    color = tim.color(random_color())
    move = rd.choice(moves)
    move()

screen.exitonclick()