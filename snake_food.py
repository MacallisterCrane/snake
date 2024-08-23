from turtle import Turtle, Screen
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.r_food()
    def r_food(self):
        rand_x = random.randint(-275, 275)
        rand_y = random.randint(-275, 275)
        self.goto(rand_x, rand_y)

