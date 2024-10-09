"""
Create a program that reads the length and width of a farmer’s field from the user in
feet. Display the area of the field in acres.
"""

SQFT_PER_ACRE = 43560
length = float(input("Enter the length of the field in feet: "))
width = float(input("Enter the width of the field in feet: "))
acres = length * width / SQFT_PER_ACRE
print(f"The area of the field is {acres} acres.")
