from sys import argv

script, filename = argv

print("This is the study drill script that uses read and argv.")
print(f"It will now open and display the contents of {filename}.")

file = open(filename)

print(file.read())