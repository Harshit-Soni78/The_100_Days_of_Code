"""
Write a program that determines the name of a shape from its number of sides. Read
the number of sides from the user and then report the appropriate name as part of
a meaningful message. Your program should support shapes with anywhere from 3
up to (and including) 10 sides. If a number of sides outside of these ranges are entered,
then your program should display an appropriate error message
"""

side = int(input("Enter the number of side: "))

if side > 10 or side < 3:
    print("The number of sides is not supported by this program.")
elif side == 3:
    print("That's a Triangle")
elif side == 4:
    print("That's a Square")
elif side == 5:
    print("That's a Pentagon")
elif side == 6:
    print("That's a Hexagon")
elif side == 7:
    print("That's a Heptagon")
elif side == 8:
    print("That's a Octagon")
elif side == 9:
    print("That's a Nonagon")
elif side == 10:
    print("That's a Decagon")
