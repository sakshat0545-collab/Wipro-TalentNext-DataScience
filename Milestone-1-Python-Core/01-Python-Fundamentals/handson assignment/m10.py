"""
Program 10:
Check whether a given number
is a palindrome.
"""

# Taking input
num = int(input("Enter a number: "))

original = num
reverse = 0

# Reverse the number
while num > 0:

    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

# Compare original and reversed numbers
if original == reverse:
    print(original, "is a Palindrome")
else:
    print(original, "is Not a Palindrome")