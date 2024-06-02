from turtle import Turtle
import time


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.curr_heading = 0

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
        self.curr_heading = self.segments[0].heading()
        time.sleep(0.1)

        for i in range(len(self.segments)-1, 0, -1):
            new_pos = self.segments[i - 1].pos()
            self.segments[i].goto(new_pos[0], new_pos[1])
        self.segments[0].fd(20)

    def go_left(self):
        match self.curr_heading:
            case 90:
                self.segments[0].lt(90)
            case 270:
                self.segments[0].rt(90)

    def go_right(self):
        match self.curr_heading:
            case 90:
                self.segments[0].rt(90)
            case 270:
                self.segments[0].lt(90)

    def go_up(self):
        match self.curr_heading:
            case 0:
                self.segments[0].lt(90)
            case 180:
                self.segments[0].rt(90)

    def go_down(self):
        match self.curr_heading:
            case 180:
                self.segments[0].lt(90)
            case 0:
                self.segments[0].rt(90)
