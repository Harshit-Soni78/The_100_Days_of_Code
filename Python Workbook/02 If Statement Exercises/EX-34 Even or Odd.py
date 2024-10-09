"""
Write a program that reads an integer from the user. Then your program should
display a message indicating whether the integer is even or odd.
"""
number = int(input("Enter the integer: "))
if number % 2 == 0:
    print("The integer is even")
else:
    print("The integer is odd")
