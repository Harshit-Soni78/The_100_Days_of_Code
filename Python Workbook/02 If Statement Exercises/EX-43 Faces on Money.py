"""
It is common for images of a country’s previous leaders, or other individuals of historical significance,
to appear on its money. The individuals that appear on banknotes in the United States are listed below.

Individual         |  Amount
George Washington  |  $1
Thomas Jefferson   |  $2
Abraham Lincoln    |  $5
Alexander Hamilton |  $10
Andrew Jackson     |  $20
Ulysses S. Grant   |  $50
Benjamin Franklin  |  $100


Write a program that begins by reading the denomination of a banknote from the
user. Then your program should display the name of the individual that appears on the
banknote of the entered amount. An appropriate error message should be displayed
if no such note exists.

While two-dollar banknotes are rarely seen in circulation in the United States,
they are a legal tender that can be spent just like any other denomination. The
United States has also issued banknotes in denominations of $500, $1,000,
$5,000, and $10,000 for public use. However, high denomination banknotes
have not been printed since 1945 and were officially discontinued in 1969. As
a result, we will not consider them in this exercise.
"""

banknote_individuals = {
    1: "George Washington",
    2: "Thomas Jefferson",
    5: "Abraham Lincoln",
    10: "Alexander Hamilton",
    20: "Andrew Jackson",
    50: "Ulysses S. Grant",
    100: "Benjamin Franklin"
}

denomination = int(input("Enter the denomination of the banknote (e.g., 1, 2, 5, 10, 20, 50, 100): "))

individual = banknote_individuals.get(denomination, "No such note exists.")

print(f"The individual on the ${denomination} banknote is {individual}.")
