import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)

screen.tracer(0)
player = Player()
cars = CarManager()
scoreboard = Scoreboard()
screen.listen()

screen.onkeypress(player.go_up,"Up")

reset_count = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    #repeadetly prints cars
    if reset_count == 0 or reset_count % 6 == 0: #creates and moves cars
        cars.create_car()
    cars.drive_left()
    reset_count += 1

    #detect a collision with car and turtle
    for car in cars.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.is_at_finish_line():
        player.go_to_start()
        scoreboard.level_up()
        cars.level_up()

screen.exitonclick()