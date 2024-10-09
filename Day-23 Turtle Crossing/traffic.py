from turtle import Turtle
import turtle
import random

turtle.colormode(cmode=255)
STARTING_MOVE = 10
MOVE_INCREMENT = 10


def car_color():
    r = random.randint(50, 250)
    g = random.randint(50, 250)
    b = random.randint(50, 250)
    new_color = (r, g, b)
    return new_color


class Traffic(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE
        self.hideturtle()

    def create_car(self):
        random_chance = random.randint(1, 4)
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_len=2, stretch_wid=0.9)
            new_car.penup()
            new_car.color(car_color())
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

