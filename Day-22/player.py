from turtle import Turtle


class Player(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.shape("square")
        self.penup()
        self.setpos(coordinates)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")

    # def create_player(self):
    #     self.shape("square")
    #     self.penup()
    #     self.setpos(self.coordinates)
    #     self.shapesize(stretch_wid=5, stretch_len=1)
    #     self.color("white")

    def up(self):
        new_y = self.ycor() + 20
        self.sety(new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.sety(new_y)
