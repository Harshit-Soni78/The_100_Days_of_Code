"""
Many people think about their height in feet and inches, even in some countries that
primarily use the metric system. Write a program that reads a number of feet from
the user, followed by a number of inches. Once these values are read, your program
should compute and display the equivalent number of centimeters.

    Hint: One foot is 12 inches. One inch is 2.54 centimeters.
"""
INCH_PER_FOOT = 12
CENTIMETER_PER_INCH = 2.54

print("Enter your Height")
feet = float(input("Number of feet: "))
inches = float(input("Number of inches: "))

height_in_centimeters = ((feet * INCH_PER_FOOT) + inches) * CENTIMETER_PER_INCH
print(f"Your Height in centimeters is : {height_in_centimeters}")
