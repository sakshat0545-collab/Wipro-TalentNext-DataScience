"""
Program 3:
Accept 10 numbers through command line arguments
and calculate the sum of prime numbers.
"""

# Importing sys module
import sys

# Function to check whether a number is prime
def is_prime(number):

    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):

        if number % i == 0:
            return False

    return True


# Variable to store sum
prime_sum = 0

# Reading all command line arguments
for value in sys.argv[1:]:

    number = int(value)

    if is_prime(number):
        prime_sum += number

# Displaying result
print("Sum of Prime Numbers =", prime_sum)