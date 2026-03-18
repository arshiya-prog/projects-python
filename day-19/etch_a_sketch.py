from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def forward():
    tim.fd(10)
def back():
    tim.backward(10)
def left():
    tim.left(10)
def right():
    tim.right(10)
def clear():
    tim.clear()

screen.listen()
screen.onkey(forward, "w")
screen.onkey(back, "s")
screen.onkey(left, "a")
screen.onkey(right, "d")
screen.onkey(clear, "c")

screen.exitonclick()