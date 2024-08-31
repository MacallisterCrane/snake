from turtle import Screen
import time
from snake import Snake
from snake_food import Food
from scoreboard import Scoreboard

scoreboard = Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("WILL YOU LIVE")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Eating snake food
    if snake.head.distance(food) < 15:
        food.r_food()
        scoreboard.new_score()
        snake.grow()

    #Wall collision
    if snake.head.xcor() >= 290 or snake.head.xcor() <= -290:
        scoreboard.game_reset()
        snake.reset()
    if snake.head.ycor() >= 290 or snake.head.ycor() <= -290:
        scoreboard.game_reset()
        snake.reset()

    #Body collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_reset()
            snake.reset()


screen.exitonclick()
