"""
Program 8:
Find the sum of all digits
of a given number.
"""

# Taking input
num = int(input("Enter a number: "))

sum_digits = 0

# Calculate sum of digits
while num > 0:

    digit = num % 10
    sum_digits += digit
    num //= 10

print("Sum of digits =", sum_digits)