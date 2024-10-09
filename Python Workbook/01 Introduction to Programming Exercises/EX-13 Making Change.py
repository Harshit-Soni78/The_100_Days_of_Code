"""
Consider the software that runs on a self-checkout machine. One task that it must be
able to perform is to determine how much change to provide when the shopper pays
for a purchase with cash.
Write a program that begins by reading a number of cents from the user as an
integer. Then your program should compute and display the denominations of the
coins that should be used to give that amount of change to the shopper. The change
should be given using as few coins as possible. Assume that the machine is loaded
with pennies, nickels, dimes, quarters, loonies and toonies.

    A one dollar coin was introduced in Canada in 1987. It is referred to as a
    loonie because one side of the coin has a loon (a type of bird) on it. The two
    dollar coin, referred to as a toonie, was introduced 9 years later. Its name is
    derived from the combination of the number two and the name of the loonie.
"""
CENTS_PER_TOONIES = 200
CENTS_PER_LOONIES = 100
CENTS_PER_QUARTER = 25
CENTS_PER_DIMES = 10
CENTS_PER_NICKELS = 5

number_of_cents = int(input("Enter the number of cents: "))
cents = number_of_cents

toonies = number_of_cents//200
number_of_cents = number_of_cents % CENTS_PER_TOONIES

loonies = number_of_cents//100
number_of_cents = (number_of_cents % CENTS_PER_LOONIES)

quarters = number_of_cents//25
number_of_cents = (number_of_cents % CENTS_PER_QUARTER)

dimes = number_of_cents//10
number_of_cents = (number_of_cents % CENTS_PER_DIMES)

nickels = number_of_cents//5
number_of_cents = number_of_cents % CENTS_PER_NICKELS
pennies = number_of_cents

print(f"""{cents} cents can be divided by:
toonies = {toonies}
loonies = {loonies}
quarters = {quarters}
dimes = {dimes}
nickels = {nickels}
pennies = {pennies}
""")
