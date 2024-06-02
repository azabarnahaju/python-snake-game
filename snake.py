from turtle import Turtle
import time


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        x, y = 20, 0
        for _ in range(3):
            t = Turtle('square')
            t.setpos(x, y)
            t.color('white')
            t.up()
            x -= 20
            self.segments.append(t)

    def move(self):
        time.sleep(0.1)

        for i in range(len(self.segments)-1, 0, -1):
            new_pos = self.segments[i - 1].pos()
            self.segments[i].goto(new_pos[0], new_pos[1])
        self.segments[0].fd(20)

    def go_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def go_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def go_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def go_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
