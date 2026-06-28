"""
Program 3:
Read a file and display its contents
in Title Case.
"""

try:
    # Taking file name from user
    filename = input("Enter file name: ")

    # Opening the file
    file = open(filename, "r")

    # Reading file contents
    content = file.read()

    # Printing in title case
    print(content.title())

    # Closing file
    file.close()

except FileNotFoundError:
    print("Error: File does not exist.")

except Exception as e:
    print("Error:", e)