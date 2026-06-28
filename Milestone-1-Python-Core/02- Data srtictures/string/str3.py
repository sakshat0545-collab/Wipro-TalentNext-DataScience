"""
Program 3:
Return a new string made of n copies
of the first two characters.
"""

# Taking input
text = input("Enter a string: ")

# First two characters
first_two = text[:2]

# Length of the string
length = len(text)

# Repeat first two characters
result = first_two * length

print("Output:", result)