"""
Program 5:
Create a dictionary where
keys are numbers from 1 to 15
and values are their squares.
"""

# Creating an empty dictionary
square = {}

# Using loop
for i in range(1, 16):
    square[i] = i ** 2

print(square)