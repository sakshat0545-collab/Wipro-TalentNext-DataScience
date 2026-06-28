"""
Program 2:
Read the first n lines
from a text file.
"""

# Taking number of lines as input
n = int(input("Enter number of lines to read: "))

# Open the file
file = open("sample.txt", "r")

# Read and print first n lines
for i in range(n):
    line = file.readline()

    if not line:
        break

    print(line, end="")

# Close the file
file.close()