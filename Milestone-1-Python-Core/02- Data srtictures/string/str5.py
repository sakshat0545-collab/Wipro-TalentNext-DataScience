"""
Program 5:
Return a string made of n repetitions
of the last n characters.
"""

# Taking input
text = input("Enter a string: ")

# Taking n as input
n = int(input("Enter value of n: "))

# Last n characters
last_part = text[-n:]

# Repeat last part n times
result = last_part * n

print("Output:", result)