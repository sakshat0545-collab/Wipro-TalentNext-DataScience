"""
Program 5:
Find the longest word
from a text file.
"""

# Open the file
file = open("sample.txt", "r")

# Read all words
words = file.read().split()

# Close the file
file.close()

# Find the longest word
longest = max(words, key=len)

print("Longest Word:", longest)