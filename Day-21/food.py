from turtle import Turtle
import random
import scoreboard
class Food(Turtle):  # generate random piece of food on the board

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=.5, stretch_len=.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)