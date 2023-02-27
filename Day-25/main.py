import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")

screen.addshape("blank_states_img.gif")

turtle.shape("blank_states_img.gif")

score = 0
state_data = pandas.read_csv("50_states.csv")
states = state_data["state"]
states = states.tolist()

guessed_states = []
x = state_data["x"]
y = state_data["y"]
while guessed_states != states:
    answer_state = screen.textinput(title=f"{score}/50 States Correct",prompt="What's another state's name?")
    if answer_state == "Exit":
        unguessed_states = [state.capitalize() for state in states if state not in guessed_states]
    # if answer_state == "Exit":
    #     for state in guessed_states:
    #         states.remove(state)
    #     unguessed_states = pandas.DataFrame(states)
    #     unguessed_states.to_csv("states_to_learn.csv")
        unguessed_data = pandas.DataFrame(unguessed_states)
        unguessed_data.to_csv("states_to_learn.csv")
        break
    if answer_state.capitalize() in states and answer_state.capitalize() not in guessed_states:
        answer_state = answer_state.capitalize()
        guessed_states.append(answer_state)
        score+=1
        index = states.index(answer_state)
        state_write = turtle.Turtle()
        state_write.hideturtle()
        state_write.penup()
        state_write.setpos(x[index],y[index])
        state_write.write(answer_state,True, align="center", font =('Arial',8,'normal'))
    else:
        pass




# def get_mouse_click_coor(x,y): #used to get coordinates of each state based on my click
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

#screen.exitonclick()