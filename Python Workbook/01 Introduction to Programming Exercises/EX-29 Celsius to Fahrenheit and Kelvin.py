"""
Write a program that begins by reading a temperature from the user in degrees
Celsius. Then your program should display the equivalent temperature in degrees
Fahrenheit and degrees Kelvin. The calculations needed to convert between different
units of temperature can be found on the internet.
"""
temp_in_celsius = float(input("Enter the temperature (in Celsius): "))

temp_in_kelvin = temp_in_celsius + 273.15
temp_in_fahrenheit = (temp_in_kelvin * 9/5) + 32

print(f"""Temperature in Celsius: {temp_in_celsius}
Temperature in Fahrenheit: {temp_in_fahrenheit}
Temperature in Kelvin: {temp_in_kelvin}""")
