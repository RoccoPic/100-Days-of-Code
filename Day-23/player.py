from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
#turtle can only move forward not backward

class Player(Turtle): #controls our turtle
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setpos(STARTING_POSITION)
        self.setheading(90)


    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.setpos(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False