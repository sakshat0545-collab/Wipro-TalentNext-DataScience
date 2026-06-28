"""
Program 6:
Write a program to check whether
a given number is Prime or Not.
"""

# Taking input
num = int(input("Enter a number: "))

# Numbers less than 2 are not prime
if num < 2:
    print("Not Prime")
else:
    is_prime = True

    # Check divisibility
    for i in range(2, int(num ** 0.5) + 1):

        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime")
    else:
        print("Not Prime")