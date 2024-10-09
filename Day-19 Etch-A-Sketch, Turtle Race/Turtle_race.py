import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)
colors = ['red', 'blue', 'green', 'yellow', 'purple', 'black', 'orange']
all_turtles = []


def turtle_row(x, y, color):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x, y)
    all_turtles.append(new_turtle)


def make_turtle_row():
    for turtle_index in range(7):
        turtle_row(-230, -150 + turtle_index * 50, colors[turtle_index])


def play_racing_turtles():
    make_turtle_row()
    is_race_on = False

    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()

    if user_bet:
        is_race_on = True

    while is_race_on:
        for racing_turtle in all_turtles:
            if racing_turtle.xcor() > 230:
                is_race_on = False
                winning_color = racing_turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                else:
                    print(f"You've lost! The {winning_color} turtle is the winner!")
            random_distance = random.randint(0, 10)
            racing_turtle.forward(random_distance)


play_racing_turtles()
screen.exitonclick()
