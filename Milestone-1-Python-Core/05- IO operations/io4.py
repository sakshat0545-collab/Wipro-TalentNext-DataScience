"""
Program 4:
Read contents from a text file
line by line and store each line in a list.
"""

# Open the file
file = open("sample.txt", "r")

# Read all lines into a list
lines = file.readlines()

# Close the file
file.close()

# Display the list
print("Lines stored in list:")

for line in lines:
    print(line.strip())