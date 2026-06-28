"""
Program 1:
Remove a given item from a set.
"""

# Creating a sample set
numbers = {10, 20, 30, 40, 50}

print("Original Set:", numbers)

# Taking input from the user
item = int(input("Enter the item to remove: "))

# Check if the item exists before removing
if item in numbers:
    numbers.remove(item)
    print("Updated Set:", numbers)
else:
    print("Item not found in the set.")