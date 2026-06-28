"""
Program 3:
Given two non-negative integers,
print True if they have the same last digit,
otherwise print False.
"""

# Taking input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Finding last digit using modulus operator
last_digit1 = num1 % 10
last_digit2 = num2 % 10

# Comparing last digits
if last_digit1 == last_digit2:
    print(True)
else:
    print(False)