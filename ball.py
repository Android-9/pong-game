from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('white')
        self.x_move = 3
        self.y_move = 3

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def rebound_y(self):
        self.y_move *= -1

    def rebound_x(self):
        self.x_move *= -1
        self.x_move *= 1.1

    def reset_position(self):
        self.x_move = 3
        self.home()
        self.rebound_x()




