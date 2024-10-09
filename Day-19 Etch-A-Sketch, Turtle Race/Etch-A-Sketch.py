from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(50)


def move_backward():
    tim.backward(50)


def turn_left():
    tim.left(50)


def turn_right():
    tim.right(50)


def turn_circle():
    tim.circle(50, 90, steps=10)


def clear_screen():
    tim.reset()


screen.listen()
screen.onkey(fun=move_forward, key='w')
screen.onkey(fun=move_backward, key='s')
screen.onkey(fun=turn_left, key='a')
screen.onkey(fun=turn_right, key='d')
screen.onkey(fun=turn_circle, key='q')
screen.onkey(fun=clear_screen, key='c')

screen.exitonclick()
