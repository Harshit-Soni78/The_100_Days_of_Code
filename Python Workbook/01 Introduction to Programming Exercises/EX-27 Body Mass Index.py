"""
Write a program that computes the body mass index (BMI) of an individual. Your
program should begin by reading a height and weight from the user. Then it should
use one of the following two formulas to compute the BMI before displaying it. If
you read the height in inches and the weight in pounds, then body mass index is
computed using the following formula:
BMI = (weight / (height × height)) × 703.
If you read the height in meters and the weight in kilograms, then body mass index
is computed using this slightly simpler formula:
BMI = weight / (height × height).
"""
height = float(input("Enter your height (in meters): "))
weight = float(input("Enter your weight (in kilograms): "))

BMI = weight / height**2

print(f"Your BMI is {BMI:.2f}")
