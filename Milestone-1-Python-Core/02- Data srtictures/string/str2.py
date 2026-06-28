"""
Program 2:
Check whether a given string
is a palindrome.
"""

# Taking input
text = input("Enter a string: ")

# Reverse the string
reverse = text[::-1]

# Compare original and reversed strings
if text == reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")