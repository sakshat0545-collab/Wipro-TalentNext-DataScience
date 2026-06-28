"""
Program 3:
Check whether a given key
exists in a dictionary.
"""

# Creating a sample dictionary
student = {
    101: "Rahul",
    102: "Amit",
    103: "Priya"
}

# Taking key as input
key = int(input("Enter key to search: "))

# Checking key
if key in student:
    print("Key exists in the dictionary.")
else:
    print("Key does not exist.")