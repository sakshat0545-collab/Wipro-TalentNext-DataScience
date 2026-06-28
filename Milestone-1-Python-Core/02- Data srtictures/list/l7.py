"""
Program 7:
Remove the item from
a specified index.
"""

# Creating a list
numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

# Taking index from user
index = int(input("Enter index to remove: "))

# Check if index is valid
if 0 <= index < len(numbers):
    removed = numbers.pop(index)
    print("Removed Element:", removed)
    print("Updated List:", numbers)
else:
    print("Invalid Index")