"""
A bakery sells loaves of bread for $3.49 each. Day old bread is discounted by 60
percent. Write a program that begins by reading the number of loaves of day-old
bread being purchased from the user. Then your program should display the regular
price for the bread, the discount because it is a day old, and the total price. All the
values should be displayed using two decimal places, and the decimal points in all
the numbers should be aligned when reasonable values are entered by the user.
"""
BREAD_PRICE = 3.49
DISCOUNT = 0.6

loaves = int(input("Enter the number of loaves of day-old bread: "))

regular_cost = BREAD_PRICE * loaves
discount = regular_cost * DISCOUNT
total_cost = regular_cost - discount

print(f"""The regular price for the bread ${regular_cost:.2f}
The discount ${discount:.2f}
The total price ${total_cost:.2f}""")
