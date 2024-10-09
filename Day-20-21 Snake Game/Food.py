from turtle import Turtle
import turtle
import random

turtle.colormode(cmode=255)


def food_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    new_color = (r, g, b)
    return new_color


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.SHAPE = 'circle'
        self.shape(self.SHAPE)
        self.penup()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.speed('fastest')
        self.prev_color = self.refresh()

    def refresh(self):
        new_color = food_color()
        self.color(new_color)
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        return new_color
