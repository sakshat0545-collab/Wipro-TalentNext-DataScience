"""
Program 4:
Check whether the number at a given
index is positive or negative.
Handle invalid index exception.
"""

# List containing 10 integers
numbers = [10, -20, 35, -40, 55, -60, 70, -80, 90, -100]

try:
    # Taking index from user
    index = int(input("Enter index (0-9): "))

    # Accessing element
    value = numbers[index]

    if value >= 0:
        print(value, "is Positive")
    else:
        print(value, "is Negative")

except IndexError:
    print("Error: Invalid index.")

except ValueError:
    print("Error: Please enter a valid integer.")

except Exception as e:
    print("Error:", e)