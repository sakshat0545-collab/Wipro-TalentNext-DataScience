"""
Program 3:
Accept input from the user
and append it to a text file.
"""

# Taking input from the user
text = input("Enter text to append: ")

# Open file in append mode
file = open("sample.txt", "a")

# Write new text into the file
file.write("\n" + text)

# Close the file
file.close()

print("Data appended successfully.")