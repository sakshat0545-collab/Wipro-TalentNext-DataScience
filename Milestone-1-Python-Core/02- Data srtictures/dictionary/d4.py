"""
Program 4:
Print keys, values,
and key-value pairs.
"""

# Creating a dictionary
student = {
    "Name": "Sakshat",
    "Age": 20,
    "Course": "CSE"
}

# Printing keys
print("Keys:")
for key in student.keys():
    print(key)

# Printing values
print("\nValues:")
for value in student.values():
    print(value)

# Printing both keys and values
print("\nKey : Value")
for key, value in student.items():
    print(key, ":", value)