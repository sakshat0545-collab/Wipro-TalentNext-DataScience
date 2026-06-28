"""
Program 9:
Reverse a given number.
"""

# Taking input
num = int(input("Enter a number: "))

original = num
reverse = 0

# Reverse the digits
while num > 0:

    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print("Reversed Number =", reverse)