"""
Program 2:
Check whether an element
exists in a tuple.
"""

# Creating a sample tuple
numbers = (10, 20, 30, 40, 50)

# Taking input from the user
element = int(input("Enter element to search: "))

# Checking whether the element exists
if element in numbers:
    print("Element exists in the tuple.")
else:
    print("Element does not exist in the tuple.")