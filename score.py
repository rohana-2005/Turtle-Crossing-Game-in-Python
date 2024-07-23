from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Score(Turtle):
    def __init__(self):
        self.s = 0
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-230, 250)
        self.write(f"Level: {self.s}", align="center", font=("Courier", 15, "normal"))

    def update_score(self):
        self.clear()
        self.s += 1
        self.write(f"Level: {self.s}", align="center", font=("Courier", 15, "normal"))

    def over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courier", 15, "normal"))
        self.goto(0, -30)
        self.write(f"Score: {self.s}", align="center", font=("Courier", 15, "normal"))
