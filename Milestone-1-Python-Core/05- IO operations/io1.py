"""
Program 1:
Read the entire content from a text file
and display it to the user.
"""

# Open the file in read mode
file = open("sample.txt", "r")

# Read the complete content
content = file.read()

# Display the content
print(content)

# Close the file
file.close()