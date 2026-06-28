"""
Program 2:
Write a program to check whether a given number
is Odd or Even.
"""

# Taking input
num = int(input("Enter a number: "))

# Using modulus operator to check divisibility by 2
if num % 2 == 0:
    print("Even")
else:
    print("Odd")