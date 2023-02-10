from turtle import Turtle, Screen
from random import randint
#first you get prompted asking who will win, purple, blue, green, yellow, orange, and red
#as soon as a turtle crosses the line then to the console will print if we win or lose
is_race_on = False
gameScreen = Screen()

gameScreen.setup(width=500,height=400) #sets up the screen dimensions
#-250 and 250 for x axis and 200 and -200 for the y axis
user_bet = gameScreen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ") #returns a string
colors = ["purple","blue","green","yellow","orange","red"]
y_axis = [100, 75, 50, 25, 0,-25]
all_turtles = []

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-225,y=y_axis[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = randint(0,10)
        turtle.forward(rand_distance)

# purple = Turtle(shape="turtle")
# purple.penup()
# purple.color("purple")
# purple.goto(x=-225,y=100)

#
# blue = Turtle(shape="turtle")
# blue.penup()
# blue.color("blue")
# blue.goto(x=-225,y=75)

#
# green = Turtle(shape="turtle")
# green.penup()
# green.color("green")
# green.goto(x=-225,y=50)

#
# yellow = Turtle(shape="turtle")
# yellow.penup()
# yellow.color("yellow")
# yellow.goto(x=-225,y=25)

#
# orange = Turtle(shape="turtle")
# orange.penup()
# orange.color("orange")
# orange.goto(x=-225,y=0)

#
# red = Turtle(shape="turtle")
# red.penup()
# red.color("red")
# red.goto(x=-225,y=-25)



gameScreen.exitonclick()