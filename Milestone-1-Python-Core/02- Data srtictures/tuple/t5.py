"""
Program 5:
Replace the last value of each tuple
in a list with 100.
"""

# Creating a list of tuples
sample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

print("Original List:")
print(sample_list)

# Creating a new list
updated_list = []

# Replacing the last element of every tuple
for item in sample_list:

    # Keep the first two elements and replace the last with 100
    new_tuple = item[:-1] + (100,)
    updated_list.append(new_tuple)

print("\nUpdated List:")
print(updated_list)