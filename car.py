from turtle import Turtle
import random

colors = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')


class Car:
    def __init__(self):
        self.number_cars = []
        self.car_speed = 0.1

    def add_car(self):
        random_num = random.randint(1, 6)
        if random_num == 1:
            car = Turtle()
            car.penup()
            car.shape('square')
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(colors))
            random_y = random.randint(-250, 250)
            car.goto(300, random_y)
            self.number_cars.append(car)

    def move(self):
        for car in self.number_cars:
            car.backward(5)


