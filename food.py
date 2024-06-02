from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('purple')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed('fastest')
        self.create_new_food()

    def create_new_food(self):
        self.goto(random.randrange(-280, 280), random.randrange(-280, 280))
