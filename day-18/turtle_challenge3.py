from turtle import Turtle, Screen
import turtle
import random as rd

tim = Turtle()
screen = Screen()

turtle.colormode(255)

def color_generator():
    r = rd.randint(0, 255)
    g = rd.randint(0, 255)
    b = rd.randint(0, 255)

    return (r, g, b)


no_of_sides = 3

def draw_shape(num_sides):
    sum_angle = 180

    angle = ((num_sides - 2) * sum_angle) / num_sides
    outer_angle = 180 - angle
    
    for i in range(num_sides):
        tim.forward(100)
        tim.left(outer_angle)


for j in range(3, 11):
    tim.color(color_generator())
    draw_shape(no_of_sides)

    if no_of_sides < 11:
        no_of_sides += 1


screen.exitonclick()