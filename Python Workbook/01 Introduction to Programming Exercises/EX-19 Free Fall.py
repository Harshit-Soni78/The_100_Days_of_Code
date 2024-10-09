"""
Create a program that determines how quickly an object is traveling when it hits the
ground. The user will enter the height from which the object is dropped in meters (m).
Because the object is dropped, its initial speed is 0 m/s. Assume that the acceleration
due to gravity is 9.8 m/s^2. You can use the formula vf = sqrt(vi^2 + 2*a*d) to compute the
final speed, vf, when the initial speed, vi, acceleration, a, and distance, d, are known.
"""
from math import sqrt

a = 9.8

height = float(input("Enter the height from which the object is dropped in meters (m): "))

vf = sqrt(2 * a * height)
print(f"The speed it will be hitting the ground is: {vf:.2f} m/s")
