"""
Pretend that you have just opened a new savings account that earns 4 percent interest
per year. The interest that you earn is paid at the end of the year, and is added
to the balance of the savings account. Write a program that begins by reading the
amount of money deposited into the account from the user. Then your program should
compute and display the amount in the savings account after 1, 2, and 3 years. Display
each amount so that it is rounded to 2 decimal places.
"""
INTEREST = 0.04
first_year = float(input("Enter the amount deposited into the account 1st year: "))
second_year = float(input("Enter the amount deposited into the account 2nd year: "))
third_year = float(input("Enter the amount deposited into the account 3rd year: "))

interest_in_first_year = first_year * INTEREST
amount_in_first_year = first_year + interest_in_first_year

interest_in_second_year = (amount_in_first_year + second_year) * INTEREST
amount_in_second_year = amount_in_first_year + second_year + interest_in_second_year

interest_in_third_year = (amount_in_second_year + third_year) * INTEREST
amount_in_third_year = amount_in_second_year + third_year + interest_in_third_year

print(f"""
Amount after First year: {amount_in_first_year:.2f}
Amount after Second year: {amount_in_second_year:.2f}
Amount after Third year: {amount_in_third_year:.2f}
""")
