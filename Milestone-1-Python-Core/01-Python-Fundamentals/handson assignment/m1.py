"""
Program 1:
Write a program to check whether a given number is
Positive, Negative or Zero.
"""

# Taking input from the user
num = int(input("Enter a number: "))

# Checking the value of the number
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")