from turtle import Turtle
STARTING_POSITION = (350, 0)


class Paddle(Turtle):

    def __init__(self, coordinates):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(coordinates)

    def go_up(self):
        y_pos = self.ycor() + 20
        self.goto(self.xcor(), y_pos)

    def go_down(self):
        y_pos = self.ycor() - 20
        self.goto(self.xcor(), y_pos)
