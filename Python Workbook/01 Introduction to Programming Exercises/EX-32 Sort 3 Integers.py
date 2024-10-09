"""
Create a program that reads three integers from the user and displays them in sorted
order (from smallest to largest). Use the min and max functions to find the smallest
and largest values. The middle value can be found by computing the sum of all three
values, and then subtracting the minimum value and the maximum value.
"""
first = int(input("Enter first integer: "))
second = int(input("Enter second integer: "))
third = int(input("Enter third integer: "))

smallest = min(first, second, third)
largest = max(first, second, third)
middle = first + second + third - smallest - largest

print(f"""Current order is ({first}, {second}, {third})
Sorted order is ({smallest}, {middle}, {largest})""")
