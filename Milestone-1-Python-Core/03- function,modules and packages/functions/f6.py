"""
Program 6:
Check whether a number
is prime or not.
"""

# Function definition
def is_prime(number):

    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):

        if number % i == 0:
            return False

    return True

# Taking input
number = int(input("Enter a number: "))

# Calling the function
if is_prime(number):
    print(number, "is a Prime Number")
else:
    print(number, "is Not a Prime Number")