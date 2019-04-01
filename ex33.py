i = 0
numbers = []
stop_index = 6
increment_by = 1

def increment_append(numbers, number, increment):
  print(f"At the top i is {number}.")
  numbers.append(number)
  number += increment
  print("Numbers now: ", numbers)
  print(f"At the bottom i is {number}")
  return number


for i in range(0, stop_index):
  # apparentl for-loop resets i on each iteration?
  i = increment_append(numbers, i, increment_by) 


# original exercise loop
#while i < 6:
  #print(f"At the top i is {i}")
  #numbers.append(i)

  #i = i + 1
  #print("Numbers now: ", numbers)
  #print(f"At the bottom i is {i}")


print("The numbers: ")

for num in numbers:
  print(num)