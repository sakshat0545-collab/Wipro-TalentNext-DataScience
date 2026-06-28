"""
Program 4:
Count uppercase and lowercase
letters in a string.
"""

# Function definition
def count_letters(text):

    upper = 0
    lower = 0

    for ch in text:

        if ch.isupper():
            upper += 1

        elif ch.islower():
            lower += 1

    print("Uppercase Letters:", upper)
    print("Lowercase Letters:", lower)

# Taking input
text = input("Enter a string: ")

# Calling the function
count_letters(text)