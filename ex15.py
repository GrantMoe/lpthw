# imports the argv module from sys
from sys import argv

# assigns variables from arguments
script, filename = argv

# gets file object using filename
txt = open(filename)

# displays file's content
print(f"Here's your file {filename}:")
print(txt.read())

# closes "txt" file
txt.close()

# prompts user for filename
print("Type the filename again:")
file_again = input("> ")

# creates new file object with file_again
txt_again = open(file_again)

# prints contents of txt_again file
print(txt_again.read())

# closes txt_again file
txt_again.close()