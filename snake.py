from turtle import Turtle
START = [(0, 0), (-20, 0), (-40, 0)]
MOVE_LENGTH = 20
LEFT = 180
RIGHT = 0
UP = 90
DOWN = 270


class Snake:

    def __init__(self):
        self.segments = []
        self.create()
        self.head = self.segments[0]

    def create(self):
        for position in START:
            self.add_seg(position)

    def add_seg(self, position):
        new_snake = Turtle("square")
        new_snake.color("white")
        new_snake.pensize(11)
        new_snake.pencolor("white")
        new_snake.penup()
        new_snake.goto(position)
        self.segments.append(new_snake)

    def grow(self):
        self.add_seg(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(MOVE_LENGTH)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

