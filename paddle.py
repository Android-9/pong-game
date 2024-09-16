from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, starting_position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setposition(starting_position)

    def up(self):
        new_y = self.ycor() + 20
        self.sety(new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.sety(new_y)



