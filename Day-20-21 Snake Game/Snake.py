from turtle import Turtle
import turtle
turtle.colormode(cmode=255)
STARTING_POSITIONS = [(0, 0), (-20, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_LENGTH = 2
SHAPE = 'triangle'


class Snake:
    def __init__(self):
        self.LENGTH = STARTING_LENGTH
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
            self.segments[0].shape(SHAPE)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def extend(self, tail_color='white'):
        new_segment = Turtle("square")
        new_segment.color(tail_color)
        new_segment.penup()
        new_x = self.segments[self.LENGTH - 1].xcor()
        new_y = self.segments[self.LENGTH - 1].ycor()
        new_segment.goto(new_x, new_y)
        self.segments.append(new_segment)
        self.LENGTH += 1
