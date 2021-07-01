import time
from turtle import Screen
from car import Car
from player import Player
from scoreboard import Scoreboard


screen = Screen()
screen.title("Jacy's Turtle Crossing Game")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = Car()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(car.car_speed)
    screen.update()

    car.add_car()
    car.move()

    if player.ycor() > 290:
        scoreboard.add_level()
        car.car_speed *= 0.9
        player.goto(0, -295)

    for c in car.number_cars:
        if player.distance(c) < 30:
            scoreboard.game_over()
            game_is_on = False


screen.listen()
screen.exitonclick()
