"""
Program 2:
Check whether a number is prime or not.
Handle invalid input using exception handling.
"""

try:
    # Taking input
    number = int(input("Enter a number: "))

    if number < 2:
        print(number, "is Not a Prime Number")

    else:
        is_prime = True

        for i in range(2, int(number ** 0.5) + 1):

            if number % i == 0:
                is_prime = False
                break

        if is_prime:
            print(number, "is a Prime Number")
        else:
            print(number, "is Not a Prime Number")

except ValueError:
    print("Error: Please enter a valid integer.")