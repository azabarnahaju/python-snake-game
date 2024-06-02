from turtle import Turtle


class Score:
    def __init__(self):
        self.score = 0
        self.message = Turtle()
        self.message.ht()

    def increment(self):
        self.score += 1

    def scoreboard(self):
        self.message.clear()
        self.message.setpos(0, 270)
        self.message.color("yellow")
        self.message.write(f"Score: {self.score}", align='center', font=('Arial', 14, 'normal'))

    def game_over(self):
        self.message.up()
        self.message.goto(0, 0)
        self.message.color("red")
        self.message.write(f'GAME OVER!\nYour score: {self.score}', align='center', font=('Arial', 22, 'bold'))
