"""
Program 1:
Accept two numbers as command line arguments
and display their sum.
"""

# Importing sys module to access command line arguments
import sys

# Reading numbers from command line
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

# Calculating sum
total = num1 + num2

# Displaying result
print("Sum =", total)