import pandas
import turtle

screen = turtle.Screen()
screen.title("Indian States Game")
image = "Blank_Map_of_India.gif"
screen.addshape(image)
turtle.shape(image)

'''
# This is to mark all the coordinates of each state corresponding to turtle screen 
counter = 0

states = ["Andhra Pradesh", "Arunachal Pradesh ", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana",
          "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra",
          "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu",
          "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands",
          "Chandigarh", "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep", "Delhi",
          "Puducherry"]

states_dict = {"States": [],
               "x": [],
               "y": []}


def get_mouse_click_coordinate(x, y):
    """This function helps to print/save the coordinates of mouse clicks and name of states on the turtle screen"""
    global counter
    state = states[counter]
    states_dict["States"].append(state)
    states_dict["x"].append(x)
    states_dict["y"].append(y)
    print(f"{state} :- ({x},{y})")
    counter += 1


turtle.onscreenclick(get_mouse_click_coordinate)
turtle.mainloop()

# Making dataframe and saving into a csv file
df = pandas.DataFrame(states_dict)
df.to_csv("State_Coordinates.csv")

# !!! Comment the - screen.exitonclick()
'''

data = pandas.read_csv("State_Coordinates.csv")
all_states = data["States"].to_list()
guessed_state = []

title_msg = turtle.Turtle()
title_msg.hideturtle()
title_msg.penup()
title_msg.goto(175, 250)
title_msg.write(arg="""    India has 29 states
and 7 Union Territories""", font=("Arial Nova", 20, "bold italic"), align="center")

while len(guessed_state) < 36:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/36 Names are Correct",
                                    prompt="What's another State's Name").title()

    if answer_state == "Exit":
        missing_state = []
        for state in all_states:
            if state not in guessed_state:
                missing_state.append(state)
        missing_data = pandas.DataFrame(missing_state)
        missing_data.to_csv("States_to_Learn.csv")
        break

    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data['States'] == answer_state]
        t.goto(state_data["x"].item(), state_data["y"].item())
        t.write(answer_state, font=("Arial", 10, "bold"), align="center")
        guessed_state.append(answer_state)
