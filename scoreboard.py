from turtle import Turtle
FONT = ('Impact', 28, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.right_score = 0
        self.left_score = 0
        self.hideturtle()
        self.color('white')
        self.penup()
        self.update_scoreboard()

    def add_rscore(self):
        self.right_score += 1

    def add_lscore(self):
        self.left_score += 1

    def update_scoreboard(self):
        self.clear()
        self.setposition(-100, 260)
        self.write(self.left_score, align='center', font=FONT)
        self.setposition(100, 260)
        self.write(self.right_score, align='center', font=FONT)


