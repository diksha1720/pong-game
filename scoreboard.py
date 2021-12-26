from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.r_score = 0
        self.l_score = 0

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.r_score}", align="center", font=("Courier", 50, "normal"))
        self.goto(100, 200)
        self.write(f"{self.l_score}", align="center", font=("Courier", 50, "normal"))

    def point_r(self):
        self.r_score += 1
        self.update_score()

    def point_l(self):
        self.l_score += 1
        self.update_score()




