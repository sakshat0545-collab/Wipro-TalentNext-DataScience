"""
Program 2:
Concatenate three dictionaries
to create a new dictionary.
"""

# Creating sample dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Creating an empty dictionary
result = {}

# Adding all dictionaries into result
result.update(dic1)
result.update(dic2)
result.update(dic3)

print("Combined Dictionary:")
print(result)