import turtle
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Papyrus", 20, "normal")
class Scoreboard(Turtle):
# inherit from Turtle class, use the write method
# turtle that keeps track of the score and displays it in the program
    def __init__(self):
        super().__init__()
        self.score = 0
        self.speed("fastest")
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setpos(0,260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=(f"Score: {self.score}"),align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(arg=(f"GAME OVER"), align=ALIGNMENT, font=FONT)