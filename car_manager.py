import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 7


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            new_car.shapesize(1, 2)
            new_car.goto(300, random.randint(-250, 250))
            self.cars.append(new_car)
            move_speed = 0.1

    def car_move(self):
        for i in self.cars:
            i.forward(self.car_speed)

    def speed_update(self):
        self.car_speed += MOVE_INCREMENT