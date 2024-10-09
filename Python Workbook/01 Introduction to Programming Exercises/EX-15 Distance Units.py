"""
In this exercise, you will create a program that begins by reading a measurement
in feet from the user. Then your program should display the equivalent distance in
inches, yards and miles. Use the Internet to look up the necessary conversion factors
if you don’t have them memorized.
"""
YARD_PER_MILE = 1760
FEET_PER_YARD = 3
FEET_PER_MILE = FEET_PER_YARD * YARD_PER_MILE
INCH_PER_FOOT = 12

feets = float(input("Enter the distance in feet: "))

mile = feets // FEET_PER_MILE
feets = feets % FEET_PER_MILE

yard = feets // FEET_PER_YARD
feets = feets % FEET_PER_YARD

inches = feets * INCH_PER_FOOT

print(f"""
miles = {mile}
yards = {yard}
inches = {inches}
""")
