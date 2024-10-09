from turtle import Turtle, Screen
import random
import turtle

tim = Turtle()


def tim_reset():
    tim.reset()
    tim.shape('turtle')
    tim.color('black')
    tim.speed('fastest')
    turtle.colormode(cmode=255)


def shape(side, length):
    for _ in range(side):
        tim.forward(length)
        tim.right(360 / side)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tim.pencolor((r, g, b))


def dot_painting(dot_count, list_of_color):
    tim.penup()
    tim.hideturtle()
    tim.setheading(225)
    tim.forward(250)
    tim.setheading(0)
    for dots in range(1, dot_count + 1):
        tim.dot(20, random.choice(list_of_color))
        tim.forward(50)
        if dots % 10 == 0:
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(180)
            tim.forward(500)
            tim.setheading(0)


def random_walk(number_of_steps, size, length):
    tim.pensize(size)
    for _ in range(number_of_steps):
        # tim.pencolor(random.choice(darker_colors+colors))
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        tim.pencolor((r, g, b))
        tim.forward(length)
        direction = random.randint(0, 1)
        if direction == 1:
            tim.left(90)
        else:
            tim.right(90)
        tim.forward(length)


def draw_spirograph(size_of_gap, radius=100):
    for _ in range(int(360 / size_of_gap)):
        random_color()
        tim.circle(radius)
        tim.setheading(tim.heading() + size_of_gap)


screen = Screen()
colors = [
    'red', 'orange', 'yellow', 'green', 'blue', 'purple',
    'cyan', 'magenta', 'pink', 'brown', 'light blue',
    'lime', 'teal', 'indigo', 'violet', 'maroon',
    'olive', 'navy', 'gold', 'silver', 'gray',
    'black', 'black', 'salmon', 'turquoise', 'orchid',
    'coral', 'lime green', 'sky blue', 'lavender', 'tan',
    'chocolate', 'slate gray', 'dark green', 'royal blue',
    'hot pink', 'sienna', 'aquamarine', 'dark violet',
    'medium orchid', 'pale green', 'cadet blue', 'tomato',
    'goldenrod', 'medium slate blue', 'dark orange', 'khaki',
    'medium sea green', 'firebrick'
]
darker_colors = [
    'red', 'orange', 'yellow', 'green', 'blue',
    'purple', 'brown', 'gray', 'black', 'navy',
    'maroon', 'darkgreen', 'darkblue', 'indigo',
    'darkred', 'darkorange', 'darkgoldenrod', 'darkcyan',
    'darkmagenta', 'sienna', 'darkslategray', 'darkolivegreen',
    'darkorchid', 'saddlebrown', 'darkseagreen', 'darkviolet',
    'darkturquoise', 'darkkhaki', 'darkslateblue', 'firebrick',
    'darkgray', 'midnightblue', 'darkcyan', 'darkslategray',
    'darkgreen', 'darkmagenta', 'darkorange', 'darkorchid',
    'darkred', 'darkseagreen', 'darkslateblue', 'darkturquoise',
    'darkviolet', 'dimgray', 'olivedrab', 'rosybrown', 'slategray'
]
color_list = [(241, 231, 209), (220, 160, 74), (243, 228, 236), (231, 237, 245), (233, 243, 236), (175, 68, 52),
              (63, 118, 163), (235, 203, 82), (54, 96, 60), (178, 171, 41), (176, 53, 60), (220, 173, 198),
              (209, 90, 61), (205, 163, 185), (48, 48, 95), (37, 38, 75), (128, 157, 185), (37, 83, 45), (77, 130, 185),
              (149, 169, 153)]

tim_reset()
for sides in range(3, 11):
    shape(sides, 100)
    tim.color(random.choice(colors))
tim_reset()
for _ in range(50):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
tim_reset()
for j in range(4):
    for _ in range(5):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()
    tim.left(90)
tim_reset()
for j in range(4):
    for i in range(10):
        for _ in range(2):
            tim.forward(10)
            tim.color('white')
            tim.forward(10)
            tim.color('darkred')
    tim.left(90)
tim_reset()
draw_spirograph(5)
tim_reset()
random_walk(200, 15, 30)
tim_reset()
dot_painting(100, colors + darker_colors)
tim_reset()

screen.exitonclick()
