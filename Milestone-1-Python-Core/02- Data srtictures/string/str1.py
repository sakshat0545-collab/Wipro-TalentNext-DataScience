"""
Program 1:
Count the number of uppercase
and lowercase letters in a string.
"""

# Taking input from the user
text = input("Enter a string: ")

# Variables to store counts
upper_count = 0
lower_count = 0

# Traversing each character in the string
for ch in text:

    # Check for uppercase letter
    if ch.isupper():
        upper_count += 1

    # Check for lowercase letter
    elif ch.islower():
        lower_count += 1

# Displaying the result
print("Uppercase Letters:", upper_count)
print("Lowercase Letters:", lower_count)