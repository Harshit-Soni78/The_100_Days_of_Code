"""
Develop a program that reads a four-digit integer from the user and displays the sum
of the digits in the number. For example, if the user enters 3141, then your program
should display 3+1+4+1=9.
"""
number = int(input("Enter the 4 digit integer: "))
once = number % 10
number = number // 10

tens = number % 10
number = number // 10

hundredth = number % 10
number = number // 10

thousand = number % 10
number = number // 10

sum_of_digits = once + tens + hundredth + thousand

print(f"the sum of the digits in the number is: {sum_of_digits}")

