from turtle import Screen
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
next_level = 10
speed = 0.1

is_game_on = True
while is_game_on:
    screen.update()
    screen.listen()
    score.scoreboard()

    screen.onkey(key='a', fun=snake.go_left)
    screen.onkey(key='s', fun=snake.go_down)
    screen.onkey(key='w', fun=snake.go_up)
    screen.onkey(key='d', fun=snake.go_right)

    snake.move(speed)

    if snake.head.distance(food) < 15:
        food.create_new_food()
        score.increment()
        snake.grow()

    if snake.has_bit_itself() or snake.has_hit_wall():
        is_game_on = False

    if score.score == next_level:
        next_level += 10
        speed -= 0.01

score.game_over()
screen.exitonclick()
