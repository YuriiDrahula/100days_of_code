from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 60, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.left_score}", move=False, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(f"{self.right_score}", move=False, align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def left_point(self):
        self.left_score += 1
        self.update_scoreboard()

    def right_point(self):
        self.right_score += 1
        self.update_scoreboard()
