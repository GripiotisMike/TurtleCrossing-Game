from turtle import Turtle
import random

# Define constants for the car behavior
COLORS = ["red", "blue", "yellow", "orange", "purple", "magenta", "green"]
STAT_MOVE_SPEED = 5  # Starting speed of the cars
MOVE_INCREASE = 3  # Increment in speed as the level increases

class Car:
    def __init__(self):
        """
        Initializes an empty list to hold all car objects and sets initial move speed.
        """
        self.all_cars = []  # List to store all created cars
        self.move_speed = STAT_MOVE_SPEED  # Initial movement speed of cars

    def create_car(self):
        """
        Randomly creates a car with a certain probability and adds it to the list of cars.
        The car will start at a random vertical position on the right side of the screen.
        """
        random_chance = random.randint(1, 6)  # Random chance to create a car
        if random_chance == 1:  # Only create a car 1 in 6 times
            new_car = Turtle("square")
            new_car.penup()
            new_car.speed("slow")  # Initial speed of car
            new_car.shapesize(1, 3)  # Set car dimensions (1 unit height, 3 units width)
            new_car.color(random.choice(COLORS))  # Random car color
            new_car.goto(320, random.randint(-230, 230))  # Position the car on the screen
            new_car.setheading(180)  # Point car to move left
            self.all_cars.append(new_car)  # Add the car to the list of cars

    def move_car(self):
        """
        Move each car in the list forward by the current move speed.
        """
        for car in self.all_cars:
            car.forward(self.move_speed)

    def move_increase(self):
        """
        Increase the car speed as the player progresses through levels.
        """
        self.move_speed += MOVE_INCREASE  # Increase the speed of all cars
