import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

'''
def get_mouse_click_coordinate(x,y):
    """This function helps to print the coordinates of mouse clicks on the turtle screen"""
    print(x,y)


turtle.onscreenclick(get_mouse_click_coordinate)
turtle.mainloop()

# !!! Comment the - screen.exitonclick()
'''

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 State Correct",
                                    prompt="What's another state's name").title()

    if answer_state == "Exit":
        missing_state = [state for state in all_states if state not in guessed_state]
        # missing_state = []
        # for state in all_states:
        #     if state not in guessed_state:
        #         missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("States_to_Learn.csv")
        break

    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
        guessed_state.append(answer_state)
        # t.write(state_data.state.item())

# screen.exitonclick()
