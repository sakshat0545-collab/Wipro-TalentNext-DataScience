"""
Program 5:
Print all even numbers
from a given list.
"""

# Function definition
def print_even(numbers):

    print("Even Numbers:")

    for num in numbers:

        if num % 2 == 0:
            print(num, end=" ")

# Sample list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Calling the function
print_even(numbers)