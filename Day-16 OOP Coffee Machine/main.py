# from turtle import Turtle, Screen
# timmy = Turtle()
# timmy.shape('turtle')
#
# timmy.color('green2')
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
from prettytable import PrettyTable

table = PrettyTable()
table.add_column('Pokemon Name', ['pikachu', 'charmender', 'squirtle'])
table.add_column('Type', ['Electric', 'Fire', 'Water'])
table.align = 'l'
print(table)
