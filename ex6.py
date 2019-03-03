# Assigns value of 10 to variable types_of_people
types_of_people = 10
# Creates string x using value of types_of_people
x = f"There are {types_of_people} types of people."

# Creates two more variables that are then used in creation of another formatted string
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

# Prints strings
print(x)
print(y)

# Prints strings as substrings added to string literals
print(f"I said: {x}")
print(f"I also said: '{y}'")

# Sets up a Boolean variables
hilarious = False
# Creates a formatted string WITHOUT a pre-filled variable
joke_evaluation = "Isn't that joke so funny?! {}"

# Uses .format to supply the variable to the formatted string
print(joke_evaluation.format(hilarious))

# Creates two string variables
w = "This is the left side of..."
e = "a string with a right side."

# Prints concatenation of those two strings.
print(w + e)