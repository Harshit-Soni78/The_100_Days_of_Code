"""
In the United States, fuel efficiency for vehicles is normally expressed in miles-per-gallon (MPG). In Canada,
fuel efficiency is normally expressed in liters-per-hundred kilometers (L/100 km). Use your research skills to
determine how to convert from MPG to L/100 km. Then create a program that reads a value from the user in American
units and displays the equivalent fuel efficiency in Canadian units.
"""
MPG = float(input("Enter the quantity of fuel in MPG: "))
# 1 mile = 1.609344 Km
# 1 gallon = 3.785412 litre
Liters100km = (100 * 3.785411784)/(1.609344 * MPG)
print(f"The equivalent fuel efficiency for {MPG} MPG in Canadian units is {Liters100km:.2f} L/100 km.")
