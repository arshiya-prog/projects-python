import turtle as t
import random as rd

tim = t.Turtle()
screen = t.Screen()

t.colormode(255)

tim.speed(0)

def random_color():
    r = rd.randint(0, 255)
    g = rd.randint(0, 255)
    b = rd.randint(0, 255)
    return (r, g, b)

def draw_spirograph(degree):
    initial_dir = tim.heading()
    for _ in range(int(360 / degree)):
        tim.color(random_color())
        tim.circle(100)
        tim.right(degree)

draw_spirograph(5)

screen.exitonclick()