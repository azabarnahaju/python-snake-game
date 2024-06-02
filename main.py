from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")

# Create initial snake body
x, y = -20, 0
for _ in range(3):
    t = Turtle('square')
    t.setpos(x, y)
    t.color('white')
    x += 20


screen.exitonclick()
