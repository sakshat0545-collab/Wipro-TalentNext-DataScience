"""
Program 2:
Write a function to return
the reverse of a string.
"""

# Function to reverse a string
def reverse_string(text):
    return text[::-1]

# Taking input
text = input("Enter a string: ")

# Calling the function
print("Reversed String:", reverse_string(text))