"""
The ideal gas law is a mathematical approximation of the behavior of gasses as
pressure, volume and temperature change. It is usually stated as:
PV = nRT
where P is the pressure in Pascals, V is the volume in liters, n is the amount of
substance in moles, R is the ideal gas constant, equal to 8.314 J mol/K, and T is the
temperature in degrees Kelvin.
Write a program that computes the amount of gas in moles when the user supplies
the pressure, volume and temperature. Test your program by determining the number
of moles of gas in a SCUBA tank. A typical SCUBA tank holds 12 liters of gas at
pressure of 20 million Pascals (approximately 3,000 PSI). The Room temperature is
approximately 20 degrees Celsius or 68 degrees Fahrenheit.

Hint: A temperature is converted from Celsius to Kelvin by adding 273.15
to it. To convert a temperature from Fahrenheit to Kelvin, deduct 32 from it,
multiply it by 5/9 and then add 273.15 to it.
"""
R = 8.314

pressure = float(input("Enter the pressure (in Pascals): "))
volume = float(input("Enter the volume (in Liters): "))
temp = float(input("Enter the temperature (in Celsius): "))

celsius_temp_in_kelvin = temp + 273.15
fahrenheit_temp_in_kelvin = ((temp - 32) * 5/9) + 273.15

gas_in_moles = (pressure * volume) / (R * celsius_temp_in_kelvin)

print(f"The amount of gas in moles: {gas_in_moles:.2f}")
