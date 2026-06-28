"""
Program 8:
Remove the first occurrence
of a specified element.
"""

# Creating a list
numbers = [10, 20, 30, 20, 40, 20]

print("Original List:", numbers)

# Taking element from user
element = int(input("Enter element to remove: "))

# Check if element exists
if element in numbers:
    numbers.remove(element)
    print("Updated List:", numbers)
else:
    print("Element not found in the list.")