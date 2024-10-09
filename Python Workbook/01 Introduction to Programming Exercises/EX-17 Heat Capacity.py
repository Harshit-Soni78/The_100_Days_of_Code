"""
The amount of energy required to increase the temperature of one gram of a material
by one degree Celsius is the material’s specific heat capacity, C. The total amount
of energy required to raise m grams of a material by ΔT degrees Celsius can be
computed using the formula:
q = mCΔT.

Write a program that reads the mass of some water and the temperature change
from the user. Your program should display the total amount of energy that must be
added or removed to achieve the desired temperature change.

    Hint: The specific heat capacity of water is 4.186 J/g◦C. Because water has a density
    of 1.0 gram per millilitre, you can use grams and millilitres interchangeably in this exercise.

Extend your program so that it also computes the cost of heating the water. Electricity is normally billed using
units of kilowatt-hours rather than Joules. In this exercise, you should assume that electricity costs 8.9 cents per
kilowatt-hour. Use your program to compute the cost of boiling water for a cup of coffee.

    Hint: You will need to look up the factor for converting between Joules and
    kilowatt-hours to complete the last part of this exercise.
"""
C_water = 4.186
COST_OF_ELECTRICITY = 8.9
JOULES_TO_KWH = 2.777e-7

mass_of_water = float(input("Enter mass of water: "))
temp_change = float(input("Enter the change in temperature: "))

energy = mass_of_water * C_water * temp_change
cost = energy * JOULES_TO_KWH * COST_OF_ELECTRICITY

print(f"""The total amount of energy is required is: {energy:.2f} joules.
That much energy will cost: {cost:.2f} cents.""")
