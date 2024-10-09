# import tkinter
# window = tkinter.Tk()
# window.title("My first GUI program")
# window.minsize(width=500, height=300)
#
# # Label
# my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack()
#
# window.mainloop()

# # Unlimited Argument
#
# def add(*args):
#     addition = 0
#     for n in args:
#         addition += n
#     return addition
#
#
# print(add(1, 2, 3, 4, 5, 6, 7))
#
#
# def print_args(*args):
#     print(args)
#
#
# print_args(1, 1, 2, 4, 5, 6)


# # key word argument

# def calculate(n, **kwargs):
#     n += kwargs['add']
#     n *= kwargs['multiply']
#     print(n)
#
#
# calculate(2, add=3, multiply=5)


# class Car:
#     def __init__(self, **kw):
#         self.make = kw.get("make")
#         self.model = kw.get("model")
#         self.color = kw.get("color")
#         self.seats = kw.get("seats")
#
#
# my_car = Car(make="Nissan", model="GT-R")
# print(my_car.model)

import tkinter


def button_clicked(new_text="Button got clicked"):
    print("Button got clicked")
    new_text = ui_input.get()
    my_label.config(text=new_text)


window = tkinter.Tk()
window.title("My First GUI")
window.minsize(width=500, height=500)
window.config(padx=100,pady=200)

# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)

# Button

button1 = tkinter.Button(text="Click Me", command=button_clicked)
button1.grid(column=1, row=1)


button2 = tkinter.Button(text="Click Me", command=button_clicked)
button2.grid(column=2, row=0)

# Entry Component

ui_input = tkinter.Entry(width=15)
ui_input.grid(column=3, row=2)


window.mainloop()
