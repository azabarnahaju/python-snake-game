from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

# Create initial snake body
x, y = -20, 0

segments = []

for _ in range(10):
    t = Turtle('square')
    t.setpos(x, y)
    t.color('white')
    t.up()
    x += 20
    segments.append(t)

# Move snake with keys
is_game_on = True

while is_game_on:
    screen.update()
    current_heading = segments[len(segments) - 1].heading()

    def go_left():
        match current_heading:
            case 90:
                segments[len(segments)-1].lt(90)
            case 270:
                segments[len(segments) - 1].rt(90)

    def go_right():
        match current_heading:
            case 90:
                segments[len(segments) - 1].rt(90)
            case 270:
                segments[len(segments) - 1].lt(90)

    def go_up():
        match current_heading:
            case 0:
                segments[len(segments) - 1].lt(90)
            case 180:
                segments[len(segments) - 1].rt(90)

    def go_down():
        match current_heading:
            case 180:
                segments[len(segments) - 1].lt(90)
            case 0:
                segments[len(segments) - 1].rt(90)

    screen.onkey(key='a', fun=go_left)
    screen.onkey(key='d', fun=go_right)
    screen.onkey(key='w', fun=go_up)
    screen.onkey(key='s', fun=go_down)

    screen.listen()
    time.sleep(0.3)

    for i in range(len(segments)-1):
        new_pos = segments[i + 1].pos()
        segments[i].goto(new_pos[0], new_pos[1])
    segments[len(segments) - 1].fd(20)

screen.exitonclick()
