"""
Program 1:
Accept two numbers from the user and perform division.
Handle exceptions and display an error message if required.
"""

try:
    # Taking input from the user
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # Performing division
    result = num1 / num2

    print("Result =", result)

# Handles division by zero
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# Handles invalid input
except ValueError:
    print("Error: Please enter valid integer numbers.")

# Handles any other unexpected exception
except Exception as e:
    print("Error:", e)