from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(x=-210, y=250)
        self.write(f"Level: {self.level}", move=False, align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.hideturtle()
        self.color("black")
        self.penup()
        self.setpos(0, 0)
        self.write(f"Game Over", move=False, align="center", font=FONT)