# The input() function
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# Writing Clear Prompts
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is you first name? "

name = input(prompt)
print(f"\nHello, {name}!")

# Using int() to Accept Numerical Input
age = int(input("How old are you?: "))
if age >= 18:
  print("You are old enough to vote!")
else:
  print("You are not old enough to vote!")

# Odd or Even
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
  print(f"\nThe number {number} is even.")
else:
  print(f"\nThe number {number} is odd.")
# The While Loop in Action!
current_number = 1
while current_number <= 5:
  print(current_number)
  current_number += 1

# Letting the User Choose when to Quite
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
  message = input(prompt)
  print(message)
  if message != 'quit':
    print(message)
# Using a Flag
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

active = True               # This is the flag
while active:
  message = input(prompt)
  if message == 'quit':
    active = False
  else:
    print(message)
# Using break to Exit a Loop
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
  city = input(prompt)
  if city == 'quit':
    break
  else:
    print(f"I'd love to go to {city.title()}!")
# Using continue in a Loop - Print only odd numbers
current_number = 0
while current_number < 10:
  current_number += 1
  if current_number % 2 == 0:   #<---------
    continue  # goes back to beginning
  print(current_number)

# Using continue in a Loop - Print only Even Numbers
current_number = 0
while current_number < 10:
  current_number += 1
  if current_number % 2 != 0:   #<---------
    continue  # goes back to beginning
  print(current_number)
  
# Using while loops with Lists and Dictionaries
# Moving Items from One List to Another
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
print(f"\nUnconfirmed Users: {unconfirmed_users}")
print(f"Confirmed Users: {confirmed_users}")

while unconfirmed_users:
  current_user = unconfirmed_users.pop()
  print(f"Verifying user: {current_user.title()}")
  confirmed_users.append(current_user)

confirmed_users.reverse()

print(f"Unconfirmed Users: {unconfirmed_users}")
print(f"Confirmed Users: {confirmed_users}")

# Removing All instances of Specific Values from a List
pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(f"\n{pets}")

while 'cat' in pets:
  pets.remove('cat')

print(pets)

# Filling a Dictionary with User Input
responses = {}
# Set a falg to indicate that polling is active
polling_active = True

while polling_active:
  # Prompt for the person's name and response.
  name = input("\nWhat is your name?: ")
  name.lower() # Convert input to lower case
  response = input("What do you like to do for fun?: ")
  response.lower()
  # Store the response in a dictionary
  responses[name] = response
  # Find out if anyone else is going to take the poll.
  repeat = input("Would you like to let another person respond?(yes/no): ")
  if repeat == 'no':
    polling_active = False

# Polling is complete. Show the results.
print("\n--- Pol Results ---")
for name, response in responses.items():
  print(f"{name.title()} likes to {response.title()} for fun.")