from turtle import Turtle, Screen

turtwig = Turtle()

screen = Screen()

screen.listen() #this lets us utilize our keyboard as the gui now listens to each stroke

def move_forward():
    turtwig.forward(10)

def move_backward():
    #turtwig.forward(-10) #had this originally
    turtwig.backward(10)

def turn_clockwise():
    turtwig.right(10)

def turn_counter_clockwise():
    turtwig.left(10)

def clear():
    turtwig.reset()

screen.onkey(key="w",fun=move_forward)#press w to move forward
screen.onkey(key="s",fun=move_backward)#press s to move backward
screen.onkey(key="a",fun=turn_clockwise)#press a to turn clockwise
screen.onkey(key="d",fun = turn_counter_clockwise)#press d to turn counter clockwise
screen.onkey(key="c",fun = clear)#press c to reset
screen.exitonclick()

#w to go forward, s to go backwards, a to go counter clockwise, d to go clockwise,c to clear
