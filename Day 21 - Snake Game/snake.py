from turtle import Turtle
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
DIRECTIONS = [0, 90, 180, 270]

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.setpos(position)
        self.segments.append(new_segment)

    def extend(self):
        #add a new segment to the snake.
        self.add_segment(self.segments[-1].position())
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].setpos(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DIRECTIONS[3]:
            self.head.setheading(DIRECTIONS[1])

    def down(self):
        if self.head.heading() != DIRECTIONS[1]:
            self.head.setheading(DIRECTIONS[3])

    def left(self):
        if self.head.heading() != DIRECTIONS[0]:
            self.head.setheading(DIRECTIONS[2])

    def right(self):
        if self.head.heading() != DIRECTIONS[2]:
            self.head.setheading(DIRECTIONS[0])