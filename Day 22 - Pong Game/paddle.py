from turtle import Turtle, Screen
MOVE_DISTANCE = 20

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.setpos(position)

    def up(self):
        if self.ycor() < 240:
            new_y = self.ycor() + MOVE_DISTANCE
            self.sety(new_y)

    def down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - MOVE_DISTANCE
            self.sety(new_y)