"""
Program 4:
Find the index of an item in a tuple.
"""

# Creating a sample tuple
fruits = ("Apple", "Banana", "Mango", "Orange", "Grapes")

# Taking input from the user
item = input("Enter the fruit name: ")

# Checking whether the item exists
if item in fruits:
    print("Index of", item, "is", fruits.index(item))
else:
    print("Item not found in the tuple.")