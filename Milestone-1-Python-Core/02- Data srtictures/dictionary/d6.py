"""
Program 6:
Find the sum of all values
in a dictionary.
"""

# Creating a dictionary
marks = {
    "Math": 90,
    "Science": 85,
    "English": 88,
    "Computer": 95
}

# Calculating sum
total = sum(marks.values())

print("Dictionary:", marks)
print("Sum of all values =", total)