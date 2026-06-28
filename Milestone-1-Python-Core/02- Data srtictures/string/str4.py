"""
Program 4:
Remove 'x' from the beginning
and end of a string.
"""

# Taking input
text = input("Enter a string: ")

# Remove first character if it is 'x'
if text.startswith("x"):
    text = text[1:]

# Remove last character if it is 'x'
if text.endswith("x"):
    text = text[:-1]

print("Output:", text)