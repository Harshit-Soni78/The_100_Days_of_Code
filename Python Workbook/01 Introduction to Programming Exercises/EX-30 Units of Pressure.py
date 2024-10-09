"""
In this exercise, you will create a program that reads pressure from the user in
kilopascals. Once the pressure has been read, your program should report the equivalent
pressure in pounds per square inch, millimeters of mercury and atmosphere. Use
your research skills to determine the conversion factors between these units.
"""
pressure_in_KPa = float(input("Enter the pressure (in Kilopascals): "))
pressure_in_pound_per_sq_inch = pressure_in_KPa / 6.89476
pressure_in_mmHg = pressure_in_KPa / 0.1333223684
pressure_in_atm = pressure_in_KPa / 101.325

print(f"""The equivalent pressure of {pressure_in_KPa:.2f} kilopascals is,
Pressure in pounds per square inch is {pressure_in_pound_per_sq_inch:.2f} pound/inch^2
Pressure in millimeters of mercury is {pressure_in_mmHg:.2f} mmHg
Pressure in atmosphere is {pressure_in_atm:.2f} atm
""")
