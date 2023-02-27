from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle): #controls what level we're on and prints game over when you get hit
    def __init__(self):
        super().__init__()
        self.level = 0
        self.level_up()

    def level_up(self):
        self.reset()
        self.penup()
        self.hideturtle()
        self.setpos(-280, 250)
        self.level+= 1
        self.write(arg = f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.penup()
        self.hideturtle()
        self.setpos(0, 0)
        self.write(arg="Game Over", align="center", font=FONT)