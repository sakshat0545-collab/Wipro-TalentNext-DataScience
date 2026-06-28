"""
Program 4:
Print the number of occurrences
of a specified element in a list.
"""

# Creating a list
numbers = [10, 20, 30, 20, 40, 20, 50]

print("List:", numbers)

# Taking element as input
element = int(input("Enter element to count: "))

# Counting occurrences
count = numbers.count(element)

print("Occurrences of", element, "=", count)