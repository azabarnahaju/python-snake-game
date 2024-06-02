from turtle import Screen
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

is_game_on = True
while is_game_on:
    screen.update()
    screen.listen()

    screen.onkey(key='a', fun=snake.go_left)
    screen.onkey(key='s', fun=snake.go_down)
    screen.onkey(key='w', fun=snake.go_up)
    screen.onkey(key='d', fun=snake.go_right)

    snake.move()

screen.exitonclick()
