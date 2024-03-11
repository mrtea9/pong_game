from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, coord):
        super().__init__()
        self.x, self.y = coord
        self.shape("square")


