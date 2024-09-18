from turtle import Screen
import time

from scoreboad import Scoreboard
from snake import Snake
from food import Food

screen = Screen()
screen.setup(600, 600)
# screen.bgpic("kubernetes-logo.png")
screen.bgcolor("black")
screen.title("The Snake game")
screen.tracer(0)


snake = Snake()
score = Scoreboard()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


is_game_on = True

while is_game_on:
    screen.update()
    snake.snake_move()
    time.sleep(0.1)

    # detect collision with snake

    if snake.snake_head.distance(food) < 15:
        food.move_food()
        snake.extend()
        score.increase_score()

    # detect collision with wall
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() < -280 or snake.snake_head.ycor() > 280:
        score.game_over()
        is_game_on = False


    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            is_game_on = False
            score.game_over()





screen.exitonclick()