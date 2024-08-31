from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 18, "normal")

class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.score = 0
        with open(r"C:\Users\Mac\Desktop\Python Program\snake_score.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(-51, 270)
        self.write(f"Score = {self.score}", True, align=ALIGN, font=FONT)
        self.hideturtle()
        self.update_score()

    def game_reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(r"C:\Users\Mac\Desktop\Python Program\snake_score.txt", mode="w") as data:
                 data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score = {self.score}. High Score = {self.high_score}", True, align=ALIGN, font=FONT)
        self.goto(0, 270)

    # def game_over(self):
    #     self.clear()
    #     self.penup()
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", True, align=ALIGN, font=("Arial", 24, "normal"))
    #     self.goto(0, -30)
    #     self.write(f"Score = {self.score}", True, align="center", font=("Arial", 18, "normal"))

    def new_score(self):
        self.score += 1
        self.update_score()
