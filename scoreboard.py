from turtle import Turtle

ALIGN = "center"
FONT = ("VCR OSD Mono", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        """
        Initialize the scoreboard with level 1 and display it on the screen.
        """
        super().__init__()
        self.penup()
        self.level = 1  # Starting level
        self.hideturtle()  # Hide the turtle cursor
        self.goto(-240, 260)  # Position the scoreboard
        self.shapesize(3, 3)  # Set size of the text for visibility
        self.update_score()  # Display the initial level

    def update_score(self):
        """
        Update the scoreboard to show the current level.
        """
        self.clear()  # Clear the previous score
        self.write(f"Level:{self.level}", align=ALIGN, font=FONT)

    def next_lvl(self):
        """
        Increment the level and update the scoreboard.
        """
        self.level += 1
        self.update_score()  # Update the displayed level

    def game_over(self):
        """
        Display the 'Game Over' message on the screen.
        """
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)

    def victory(self):
        """
        Display the 'Victory' message when the player wins the game.
        """
        self.goto(0, 0)
        self.write("VICTORY!", align=ALIGN, font=FONT)
