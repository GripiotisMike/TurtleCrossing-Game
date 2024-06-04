from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.goto(0, -280)
        self.setheading(90)

    def move_up(self):
        self.forward(10)

    def reset_player(self):
        self.goto(0, -280)
