"""
Program 2:
Accept a welcome message through command line arguments
and display the file name along with the welcome message.
"""

# Importing sys module
import sys

# File name
print("File Name:", sys.argv[0])

# Welcome message
print("Welcome Message:", sys.argv[1])