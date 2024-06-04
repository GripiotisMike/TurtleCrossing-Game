from turtle import Turtle
import random

COLORS = ["red", "blue", "yellow", "orange", "purple", "magenta", "green"]
STAT_MOVE_SPEED = 5
MOVE_INCREASE = 3


class Car:
    def __init__(self):
        self.all_cars = []
        self.move_speed = STAT_MOVE_SPEED

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.speed("slow")
            new_car.shapesize(1, 3)
            new_car.color(random.choice(COLORS))
            new_car.goto(320, random.randint(-230, 230))
            new_car.setheading(180)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.forward(self.move_speed)

    def move_increase(self):
        self.move_speed += MOVE_INCREASE
