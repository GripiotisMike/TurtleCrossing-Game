from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        """
        Initialize the player turtle (character) with starting position and heading.
        """
        super().__init__()
        self.penup()
        self.shape("turtle")  # Set the shape of the player to a turtle
        self.goto(0, -280)  # Start at the bottom of the screen
        self.setheading(90)  # Set initial heading to face upward

    def move_up(self):
        """
        Move the player turtle up by 10 units.
        """
        self.forward(10)

    def reset_player(self):
        """
        Reset the player turtle's position to the starting position.
        """
        self.goto(0, -280)
