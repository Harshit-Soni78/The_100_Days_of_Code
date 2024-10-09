"""
In this exercise, you will reverse the process described in the previous exercise.
Develop a program that begins by reading a number of seconds from the user.
Then your program should display the equivalent amount of time in the form
D:HH:MM:SS, where D, HH, MM, and SS represent days, hours, minutes and seconds respectively.
The hours, minutes and seconds should all be formatted so that they occupy exactly two digits,
with a leading 0 displayed if necessary.
"""
SECONDS_PER_DAY = 86400
SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTES = 60
seconds = int(input("Enter the number of seconds: "))

days = seconds // SECONDS_PER_DAY
seconds = seconds % SECONDS_PER_DAY

hours = seconds // SECONDS_PER_HOUR
seconds = seconds % SECONDS_PER_HOUR

minutes = seconds // SECONDS_PER_MINUTES
seconds = seconds % SECONDS_PER_MINUTES

print(f"The equivalent amount of time in the form D:HH:MM:SS is: {days}:{hours:02d}:{minutes:02d}:{seconds:02d}")
