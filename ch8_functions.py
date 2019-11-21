# Defining a simple function
def greet_user_simple():
  """Display a simple greeting."""       # This is a docstring. Used to generate documentation for functions in programs.
  print("Hello!")

greet_user_simple()

# Passign information to a Function
def greet_user(username):
  """Display a simple greeting to a user."""
  print(f"Hello, {username.title()}!")

greet_user('cody')

# Positional Arguments
def describe_pet(animal_type, pet_name):  
  """Display information about a pet."""
  print(f"\nI have a {animal_type}.")
  print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# Keyword argument - name-value pair that is passed to the function
describe_pet(animal_type='hamster', pet_name='harry')

# Default values
def describe_pet1(pet_name, animal_type='dog'):  
  """Display information about a pet."""
  print(f"\nI have a {animal_type}.")
  print(f"My {animal_type}'s name is {pet_name.title()}.")

# Equivalent function calls
describe_pet1(pet_name='willie')
describe_pet1('willie')
describe_pet1('harry', 'hamster')
describe_pet1(pet_name = 'harry', animal_type = 'hamster')
describe_pet1(animal_type='hamster',pet_name='harry')

# Returning a Simple Value
def get_formatted_name0(first_name, last_name):
  """Return a full name, neatly formatted."""
  full_name = f"{first_name} {last_name}"
  return full_name.title()

musician = get_formatted_name0('jimi', 'hendrix')
print(f"\n{musician}")

# Making an Argument Optional
def get_formatted_name(first_name, last_name, middle_name=''):
  """Return a full name, neatly formatted."""
  if middle_name:
    full_name = f"{first_name} {middle_name} {last_name}"
  else:
    full_name = f"{first_name} {last_name}"
  return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(f"\n{musician}")

musician = get_formatted_name('john','hooker','lee')
print(f"\n{musician}")

# Returning a Dictionary
def build_person(first_name, last_name, age=None):    # Age is optional  
  """Return a dictionary of information about a person."""
  person = {'first':first_name, 'last':last_name}
  if age:
    person['age'] = age
  return person

musician = build_person('jimi', 'hendrix', 27)
print(f"\n{musician}")

# Using a function with a while loop
while True:
  print("\nPlease tell me your name:")
  print("(enter 'q' at any time to quit)")

  f_name = input("First name: ")
  if f_name == 'q':
    break

  l_name = input("Last name: ")
  if l_name == 'q':
    break

  formatted_name = get_formatted_name(f_name,l_name)
  print(f"\nHello, {formatted_name}!")

