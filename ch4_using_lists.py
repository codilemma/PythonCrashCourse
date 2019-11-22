# Refer to PEP 8 guidelines

# Looping Through an Entire List
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
    

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

# Using the range() function
for value in range(1, 5):
    print(value)

# Use range() to make a list of numbers
numbers = list(range(1, 6))
print(numbers)

# use range() to print even numbers
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# another range() example
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

# or more concisely
squares2 = []
for value in range(1,11):
    squares2.append(value**2)
print(squares2)

# Min and Max of lists
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# List Comprehensions - combines a for loop and creating of new elements into one line
squares = [value**2 for value in range(1,11)]
print(squares)

# Slicing a List
players = ['charles', 'martina', 'micheal', 'florence', 'eli']
print(players)
print(players[0:3])
print(players[:2])  # Automatically starts at begining of list
print(players[2:])  # Starts at item #2 and goes to end the list.
print(players[-3:])  # outputs last three items in the list

# Looping through a Slice
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# Copying a List
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

# Tupple - A list of items that cannot change.  A value that cannot change is refered to as immutable.
# and an immutable list is called a tuple
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Looping through all values in a Tuple
dimensions = (200, 50, 100)            # you must redifine a tuple to write over it
for dimension in dimensions:
    print(dimension)



