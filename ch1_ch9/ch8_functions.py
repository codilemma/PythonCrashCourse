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

# Passing a list to a function
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah','ty','margot']
greet_users(usernames)

# Modifying a List in a Function
# Start with some desings that need to be printed
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

# Re-org code above into functions
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case','robot pendant','dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# Preventing a Function from Modifying a List
unprinted_designs = ['phone case','robot pendant','dodecahedron']
completed_models = []
# Sends a copy of the unprinted_designs list to the function (not efficient and should be avoided)
print_models(unprinted_designs[:], completed_models)  

# Passing an arbitrary number of arguments 
def make_pizza0(size, *toppings):  # * Instructs function to pack incoming variable data into a tuple
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza0(12, 'mushrooms','green peppers','extra cheese')

# Using Arbitrary Keword Arguments
def build_profile(first, last, **user_info):  # ** creates a dictionary
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert','einstein',
                             location='princeton',
                             field='physics')

print(user_profile)

# Storing a function in module
# Importing an Entire Module
import ch8_pizza
ch8_pizza.make_pizza(16, 'mushrooms','green peppers','extra cheese')

# Importing Specific functions from a module
# from module_name import function_0, function_1, function_2
from ch8_pizza import make_pizza
make_pizza(12,'mushrooms','green peppers','extra cheese')

# Using as to Give a Function an Alias
from ch8_pizza import make_pizza as mp
mp(12,'mushrooms','green peppers','extra cheese')

# Using as to give a module an alias
import ch8_pizza as p
p.make_pizza(16,'peperoni')

# Importing All Functions in a Module
from ch8_pizza import *
