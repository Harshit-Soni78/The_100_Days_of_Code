from turtle import Screen
import time
from Snake import Snake
from Food import Food
from scoreboard import Score

WIDTH = 600
HEIGHT = 600

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
my_score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        tail_color = food.refresh()
        my_score.increase_score()
        snake.extend(tail_color)

    # Detect collision with walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        my_score.game_over()

    # Detect collision with tail
    # if head collide with any segment except head itself in the tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 1:
            game_is_on = False
            my_score.game_over()

screen.exitonclick()
