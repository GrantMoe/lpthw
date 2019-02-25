# Assigns value of 100 to variable 'cars'
cars = 100
# Assigns value of 4.0 to variable 'space_in_a_car'
space_in_a_car = 4.0
# Assigns value of 40 to variable 'drivers' 
drivers = 30
# Assigns value of 90 to variable 'passengers'
passengers = 90
# Assigns the value of 'cars' minus the value of 'drivers' to variable 'cars_not_driven'
cars_not_driven = cars - drivers
# Assigns value of 'drivers' to the variable 'cars_driven'
cars_driven = drivers
# Assigns to variable 'carpool_capacity' the value of 'cars_driven' times 'space_in_car'
carpool_capacity = cars_driven * space_in_a_car
# Assigns to 'average_passengers_per_car' the value of 'passangers' divided by 'cars_driven'
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
      "in each car.")