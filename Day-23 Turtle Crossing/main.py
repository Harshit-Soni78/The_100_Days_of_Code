from turtle import Screen
from time import sleep
from player import Player
from traffic import Traffic
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.go_up, "Up")

traffic = Traffic()

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    sleep(0.1)
    screen.update()

    traffic.create_car()
    traffic.move_cars()

    # Detect collision with car
    for car in traffic.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # A successfully crossing
    if player.is_at_finish_line():
        player.go_to_start()
        traffic.level_up()
        scoreboard.increase_the_level()

screen.exitonclick()