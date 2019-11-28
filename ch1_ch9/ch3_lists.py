bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# Accessing Elements in a List
print(bicycles[0])
print(bicycles[0].title())

# Accessing items from the end of the list
print(bicycles[-1])  # last item in list
print(bicycles[-2])  # second to last item in list

# f strings and lists
message = f"My first bicycle was a {bicycles[0].title()}"
print(message)

# Adding Elements to the end of a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

# Inserting Elements into a List
motorcycles.insert(0, 'ducati')
print(motorcycles)

# Removing Item from List using the del Statement
del motorcycles[0]
print(motorcycles)

# Removing Item from List using the pop() method
# Allows you to remove item from the list and then use it in the application
popped_motorcycle = motorcycles.pop()  # use motorcycles.pop(number) to remove any item from list and use it
print(motorcycles)
print(popped_motorcycle)

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

# Remove item from list by value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

# Sorting a List Permanently with the sort() Method - Alphabetically
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()  # organizes the list alphabetically - this is now permanent
print(cars)

# Sort list reverse alphabetically
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort(reverse=True)
print(cars)

# Sorting a list temporarily with the sorted() Function
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the orginal list:")
print(cars)
print("\nHere is the alphabetically sorted list:")
print(sorted(cars))
print("\nHere is the orginal list again:")
print(cars)
print("\nHere is reverse alhpabetically the sorted list:")
print(sorted(cars, reverse=True))

# Reverse the order of a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

#finding the length of a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))