from turtle import Turtle


# width 20, height = 20, x_pos = 0, y_pos = 0, to start moves diagonally up right
# x and y will change on each refresh
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color('white')
        self.x_move = 10
        self.y_move = 10
        self.setpos(0, 0)
        self.penup()
        self.speed(1)
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.setpos(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *=0.9
    def ball_reset_position(self):
        self.goto(0,0)
        self.bounce_x()
        self.move_speed = 0.1