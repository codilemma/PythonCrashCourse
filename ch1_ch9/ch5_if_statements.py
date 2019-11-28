# A simple example
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
  if car == 'bmw':
      print(car.upper())
  else:
      print(car.title())    # if car != 'bmw'

# Case matters in conditional statements
car = 'Audi'
print(car == 'audi')           # returns False
print(car.lower() == 'audi')   # returns True

# Use and / or to check multiple conditions
age0 = 22
age1 = 18
print(age0 >= 21 and age1 >= 21)
print(age0 >= 21 or age1 >= 21)

# Checking if a value is in a list
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)

# Checking if value is NOT in a list
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

# The if-elif-else Chain
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else: 
    print("Your admission cost is $40.")

# Another Example
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now")
    else:
        print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")

# Checking that a list is not empty
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
        print("\nFinished making your pizza")
else:
    print("Are you sure you want a plain pizza?")

# Using multiple lists
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      ' pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")


