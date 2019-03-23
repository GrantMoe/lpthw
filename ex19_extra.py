from sys import argv

def tenwise_function(arg):
  print(f"My function! It prints {arg}!")


# 1
print("Firstwise: literal!")
tenwise_function(10)

# 2
print("Secondwise: variable!")
tenwise_variable = 10
tenwise_function(tenwise_variable)

# 3
print("Thirdwise: variable plus literal!")
tenwise_function(tenwise_variable + 10)

# 4
print("Fourthwise: literal plus literal?")
tenwise_function(5 + 5)

# 5 
print("Fifthwise: variable times variable!")
fivewise_variable = 5
tenwise_function(fivewise_variable * 2)

# 6
print("Sixthwise: SPICE THINGS UP WITH USER INPUT. FEED ME!")
tenwise_function(input())

# 7
print("I'm running out of ideas! Let's go and get argv maybe!")
tenwise_function(argv)

# 8
print("Sweet lord! Let's make a file! Let's read it to a variable, then read it!")
eighthwise_file = open("test.txt",'w')
eighthwise_file.write("10")
eighthwise_file.close()
inwise_file = open("test.txt")
inwise_data = inwise_file.read()
tenwise_function(inwise_data)
inwise_file.close()

# 9
print("Let's read it RIGHT FROM THE FILE")
tenwise_function(open("test.txt").read())

# 10
print("Let's take the string from the file, turn it into an int, then do maths!:")
tenwise_function(int(open("test.txt").read()) + int(open("test.txt").read()))