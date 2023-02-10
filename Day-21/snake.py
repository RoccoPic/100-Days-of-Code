from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):  # what happens here is how we want our initial snake to be setup
        self.segments = []
        self.create_snake()  # [0, -20, -40]
        self.head = self.segments[0]
        self.tail = self.segments[-1]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self,position):
        new_piece = Turtle("square")
        new_piece.color("white")
        new_piece.penup()
        new_piece.setpos(position)
        self.segments.append(new_piece)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
