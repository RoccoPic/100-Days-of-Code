from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(): #prints cars randomly along the y-axis and they move from the right edge to the left edge
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        random_y = random.randint(-250, 250)
        new_car.setpos(300, random_y)
        self.all_cars.append(new_car)

    def drive_left(self):
        for i in range(0,len(self.all_cars)):
            self.all_cars[i].backward(self.speed)


    def level_up(self):
        # for i in range(0,len(self.all_cars)):
        #     self.all_cars[i].reset()
        self.speed += MOVE_INCREMENT
