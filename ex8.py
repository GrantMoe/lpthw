# Creates string variable with four "slots" for variables/additions
formatter = "{} {} {} {}"

# Call formatter's .format() function with various different things to fill the slots
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
# Illustrates what happens when formatter is printed without being formatted
print(formatter.format(formatter, formatter, formatter, formatter))
# Prints the first four arguments supplied to .format()
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear",
    "This will neither print",
    "Nor cause an error"
  ))