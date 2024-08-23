from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 18, "normal")

class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score = {self.score}", True, align=ALIGN, font=FONT)
        self.hideturtle()

    def game_over(self):
        self.clear()
        self.penup()
        self.goto(0, 0)
        self.write(f"GAME OVER", True, align=ALIGN, font=("Arial", 24, "normal"))
        self.goto(0, -30)
        self.write(f"Score = {self.score}", True, align="center", font=("Arial", 18, "normal"))

    def new_score(self):
        self.clear()
        self.score += 1
        self.goto(0, 270)
        self.write(f"Score = {self.score}", True, align="center", font=("Arial", 18, "normal"))

