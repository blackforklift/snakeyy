from turtle import Screen
from snake import Snake
from food import Food
import time
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
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


#will snake meet with food

    if snake.head.distance(food) < 15:
        food.updateFood()
        score.updateScore()
        snake.grow()


#will snake hit the wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290: #screen is 600x600
       score.game_over()
       game_is_on = False

#will snake eat itself up

    for segment in snake.segments[1:]: #sliced coz if it starts with first segment a.k.a head, head will collide with head so game will start with game over
        if snake.head.distance(segment) < 10:
            game_is_on=False
            score.game_over()




screen.exitonclick()