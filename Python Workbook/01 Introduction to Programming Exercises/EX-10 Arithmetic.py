"""
Create a program that reads two integers, a and b, from the user. Your program should
compute and display:
• The sum of a and b
• The difference when b is subtracted from a
• The product of a and b
• The quotient when a is divided by b
• The remainder when a is divided by b
• The result of log10 a
• The result of a^b
"""
from math import log10
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
print(f"""
• The sum of {a} and {b} is {a+b}
• The difference when {b} is subtracted from {a} is {a-b}
• The product of {a} and {b} is {a*b}
• The quotient when {a} is divided by {b} is {int(a/b)}
• The remainder when {a} is divided by {b} is {a%b}
• The result of log10 {a} is {log10(a)}
• The result of {a}^{b} is {a**b}
""")
