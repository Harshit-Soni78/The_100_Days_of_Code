import pandas
import turtle

screen = turtle.Screen()
screen.title("Indian States Game")
image = "Blank_Map_of_India.gif"
screen.addshape(image)
turtle.shape(image)

states = ["Andhra Pradesh", "Arunachal Pradesh ", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana",
          "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra",
          "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu",
          "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands",
          "Chandigarh", "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep", "Delhi",
          "Puducherry"]
states_dict = {"States": [],
               "x": [],
               "y": []}
counter = 0


def get_mouse_click_coordinate(x, y):
    """This function helps to print the coordinates of mouse clicks on the turtle screen"""
    print(x, y)
    global counter
    state = states[counter]
    states_dict["States"].append(state)
    states_dict["x"].append(x)
    states_dict["y"].append(y)
    counter += 1


turtle.onscreenclick(get_mouse_click_coordinate)
turtle.mainloop()

df = pandas.DataFrame(states_dict)
print(df)
df.to_csv("State_Coordinates.csv")
