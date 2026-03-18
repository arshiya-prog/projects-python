# import colorgram
import turtle as t
import random as rd

# colors = colorgram.extract("/Users/arshiya/Desktop/Coding/Python/projects-python/hirst_painting/image.jpg", 30)
rgb = [(208, 160, 82), (54, 89, 131), (146, 91, 40), (140, 26, 48), (222, 206, 108), (132, 177, 203), 
       (158, 45, 83), (47, 55, 103), (167, 160, 38), (128, 189, 143), (84, 20, 44), (36, 42, 70), 
       (187, 93, 105), (187, 139, 170), (84, 123, 181), (59, 39, 31), (78, 153, 165), (88, 157, 91), (195, 79, 72), (45, 74, 78), 
       (161, 202, 220), (80, 73, 44), (57, 131, 121), (218, 176, 188), (220, 183, 166), (166, 207, 165)]

t.colormode(255)

tim = t.Turtle()
screen = t.Screen()
tim.hideturtle()

# for color in colors:
#     red = color.rgb.r
#     green = color.rgb.g
#     blue = color.rgb.b

#     tup = (red, green, blue)

#     rgb.append(tup)


def color_turtle():
    tim.color(rd.choice(rgb))
    tim.dot(20)
    tim.penup()
    tim.forward(50)

y_cor = -200
x_cor = -200
tim.speed(0)
tim.penup()

for j in range(10):
    tim.sety(y_cor)
    tim.setx(x_cor)
    for i in range(10):
        color_turtle()
    y_cor += 50

screen.exitonclick()