"""
Program 6:
Count the frequency of a
user-entered word in a text file.
"""

# Taking word from user
search_word = input("Enter word to search: ")

# Open the file
file = open("sample.txt", "r")

# Read file and split into words
words = file.read().split()

# Close the file
file.close()

# Count frequency
count = words.count(search_word)

print(f'"{search_word}" occurs {count} time(s).')