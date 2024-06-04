from turtle import Turtle

ALIGN = "center"
FONT = ("VCR OSD Mono", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 1
        self.hideturtle()
        self.goto(-240, 260)
        self.shapesize(3, 3)
        self.write(f"Level:{self.level}", align=ALIGN, font=FONT)

    def next_lvl(self):
        self.level += 1
        self.clear()
        self.write(f"Level:{self.level}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)

    def victory(self):
        self.goto(0, 0)
        self.write("VICTORY!", align=ALIGN, font=FONT)
