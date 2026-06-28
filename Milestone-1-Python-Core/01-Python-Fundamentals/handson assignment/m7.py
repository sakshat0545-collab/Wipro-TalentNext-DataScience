"""
Program 7:
Print all prime numbers between 10 and 99.
"""

# Loop through numbers from 10 to 99
for num in range(10, 100):

    is_prime = True

    # Check if current number is prime
    for i in range(2, int(num ** 0.5) + 1):

        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)