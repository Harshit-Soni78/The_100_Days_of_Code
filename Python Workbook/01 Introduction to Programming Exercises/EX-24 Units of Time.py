"""
Create a program that reads a duration from the user as a number of days, hours,
minutes, and seconds. Compute and display the total number of seconds represented
by this duration.
"""
days = int(input("Enter the no. of days: "))
hours = int(input("Enter the no. of hours: "))
minutes = int(input("Enter the no. of minutes: "))
seconds = int(input("Enter the no. of seconds: "))

seconds = seconds + (60 * minutes) + (60 * 60 * hours) + (60 * 60 * 24 * days)

print(f"The total number of seconds represented by this duration is: {seconds}")
