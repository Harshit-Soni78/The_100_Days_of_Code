"""
The surface of the Earth is curved, and the distance between degrees of longitude
varies with latitude. As a result, finding the distance between two points on the surface
of the Earth is more complicated than simply using the Pythagorean theorem.
Let (t1, g1) and (t2, g2) be the latitude and longitude of two points on the Earth’s
surface. The distance between these points, following the surface of the Earth, in
kilometers is:
distance = 6371.01 × arccos(sin(t1) × sin(t2) + cos(t1) × cos(t2) × cos(g1 − g2))
    "The value 6371.01 in the previous equation wasn’t selected at random. It is
    the average radius of the Earth in kilometers."
Create a program that allows the user to enter the latitude and longitude of two
points on the Earth in degrees. Your program should display the distance between
the points, following the surface of the earth, in kilometers.
"""
import math
t1 = float(input("Enter the first latitude: "))
g1 = float(input("Enter the first longitude: "))
t2 = float(input("Enter the second latitude: "))
g2 = float(input("Enter the second longitude: "))

distance = 6371.01 * math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1 - g2))
print(f"The distance between the points ({t1}, {g1}) and ({t2}, {g2}) is {distance:.2f} Km")
