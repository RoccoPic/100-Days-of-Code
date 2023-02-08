import turtle

from colorgram import *
from turtle import Turtle, Screen
from random import *

turtle.colormode(255)

colors = extract("hirst-painting.jpg",40)
#used to extract colors from a hirst painting reference to be able to recreate a similar painting
rgb_colors = []

for i in range(len(colors)):
    r = colors[i].rgb.r
    g = colors[i].rgb.g
    b = colors[i].rgb.b
    rgb_colors.append((r,g,b))

def colorChoice():
    color = rgb_colors[randint(0,len(rgb_colors)-1)]
    return color
def dot():
    turtwig.setx(-200)
    turtwig.sety(-200)
    turtwig.penup()
    turtwig.hideturtle()
    for i in range(100):
        if i != 0 and i % 10 == 0:
            turtwig.setx(-200)#+ ((i-1)* 10))
            turtwig.sety(-200 + ((i)* 5))
        turtwig.color(colorChoice())
        #turtwig.pendown()
        turtwig.dot(20)
        #turtwig.penup()
        turtwig.forward(50)
    turtwig.penup()

#set of colors grabbed from the original hirst painting, if we want to speed up program we can comment out the original extraction and use this list of tuples
#turtle_colors = [(61, 17, 128), (234, 23, 9), (232, 251, 242), (198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 246, 252), (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239), (81, 73, 214), (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40), (218, 87, 49), (174, 178, 231), (237, 169, 164), (6, 245, 223), (247, 9, 42), (10, 79, 112), (16, 54, 243), (240, 16, 16)]

turtwig = Turtle() #creating our cursor for our screen below
turtwig.penup()
turtwig.pensize(5)
turtwig.speed("fastest")
screen = Screen() #screen initialized
screen.title("Welcome to my Hirst Painting")
dot()

screen.exitonclick()#screen can be exited when clicked
