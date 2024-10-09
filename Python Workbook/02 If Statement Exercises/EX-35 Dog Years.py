"""
It is commonly said that one human year is equivalent to 7 dog years. However, this
simple conversion fails to recognize that dogs reach adulthood in approximately two
years. As a result, some people believe that it is better to count each of the first two
human years as 10.5 dog years, and then count each additional human year as 4 dog
years.

Write a program that implements the conversion from human years to dog years
described in the previous paragraph. Ensure that your program works correctly for
conversions of less than two human years and for conversions of two or more human
years. Your program should display an appropriate error message if the user enters
a negative number.
"""
human_years = float(input("Enter the number of human years: "))

if human_years < 0:
    print("Error: Number of years cannot be negative.")
elif human_years <= 2:
    print(f"{human_years} human years is equivalent to {human_years * 10.5} dog years.")
else:
    print(f"{human_years} human years is equivalent to {21 + (human_years - 2) * 4} dog years.")
