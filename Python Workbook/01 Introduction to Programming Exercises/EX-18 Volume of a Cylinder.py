"""
The volume of a cylinder can be computed by multiplying the area of its circular
base by its height. Write a program that reads the radius of the cylinder, along with
its height, from the user and computes its volume. Display the result rounded to one
decimal place.
"""
from math import pi

radius_of_circular_base = float(input("Enter the radius of circular base: "))
height_of_cylinder = float(input("Enter the height of the cylinder: "))

area_of_circular_base = pi * radius_of_circular_base ** 2
volume_of_cylinder = area_of_circular_base * height_of_cylinder

print(f"The volume of the cylinder having radius of circular base {radius_of_circular_base} "
      f"and height {height_of_cylinder} is: {volume_of_cylinder:.1f}.")
