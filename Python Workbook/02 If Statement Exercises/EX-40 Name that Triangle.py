"""
A triangle can be classified based on the lengths of its sides as equilateral, isosceles
or scalene. All three sides of an equilateral triangle have the same length. An isosceles
triangle has two sides that are the same length, and a third side that is a different
length. If all the sides have different lengths, then the triangle is scalene.
Write a program that reads the lengths of three sides of a triangle from the user.
Display a message indicating the type of the triangle.
"""

side1 = float(input("Enter the first side: "))
side2 = float(input("Enter the second side: "))
side3 = float(input("Enter the third side: "))

if side1 == side2 and side2 == side3:
    print(f"Following triangle is equilateral triangle of side {side1}.")
elif side1 == side2 or side2 == side3 or side3 == side1:
    print(f"Following triangle is isosceles triangle of sides ({side1}, {side2}, {side3}).")
elif side1 != side2 and side2 != side3 and side3 != side1:
    print(f"Following triangle is scalene triangle of sides ({side1}, {side2}, {side3}).")
