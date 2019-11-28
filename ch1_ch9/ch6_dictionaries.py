# A Simple Dictionary
alien_0 = {'color':'green', 'points':5}   #{key:value, key:value}
print(alien_0)
print(alien_0['color'])
print(alien_0['points'])

# Adding new Key-Vaule Pairs to Existing Dictionary
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# You can also start with empty dictionaries
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

# Modifying Values in a Dictionary
alien_0 = {'color':'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

# Tracking the Alien's movement.
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

# Removing Key-Value Pairs
alien_0 = {'color':'green', 'points':5}
print(alien_0)
del alien_0['points']
print(alien_0)

# A Dictionary of Similiar objects
favorite_languages = {'jen':'python',
                      'sarah':'c',
                      'edward':'ruby',
                      'phil':'python'}
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}")

# using get() to Access Values
alien_0 = {'color':'green', 'speed':'slow'}
# print(alien_0['points'])  - Returns a compile error because points does not exist yet
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

# Looping through all key value pairs
user_0 = {
  'username':'efermi',
  'first':'enrico',
  'last':'fermi',
  }

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"\nvalue: {value}")

# Looping though the keys only
favorite_languages = {'jen':'python',
                      'sarah':'c',
                      'edward':'ruby',
                      'phil':'python'}

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

# Check to see if a user was polled
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# Looping through keys in a particular order - Alphabetically
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the pol.")

# Looping through all values in a Dictionary
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# Use set() set to list the unique entries - omits duplicates such as 'Python'
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# The three largest rivers in the World example
rivers = {'nile':'egypt', 'amazon':'brazil', 'yangtze':'china'}

for river in rivers.keys():
    print(f"The {river.title()} river runs through {rivers[river].title()}")
#OR
for key, value in rivers.items():
    print(f"The {key.title()} river runs through {value.title()}")

# People polled example
people_polled = ['jen', 'sarah', 'edward', 'phil', 'bob']
for name in people_polled:
    if name in favorite_languages.keys():
        print(f"{name}, thank you for taking our poll!")
    if name not in favorite_languages.keys():
        print(f"{name}, please take our poll!")

# Nested Dictionaries in a list
alien_0 = {'color':'green', 'points':5}
alien_1 = {'color':'yelow', 'points':10}
alien_2 = {'color':'red', 'points':15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# Use range() to create a fleet of aliens
aliens = []
for alien_number in range(30):
    new_alien = {'color':'green', 'points':5, 'speed':'slow'}
    aliens.append(new_alien)
# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print('...')
# Show how many aliens have been created
print(f"Total numjber of alies = {len(aliens)}")

#Change the first three aliens to faster aliens
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# Storing a list in a Dictionary - Example 1
pizza = { 'crust':'thick',
          'toppings':['mushrooms', 'extra cheese'],
        }
print(f"You ordered a {pizza['crust']}-crust pizza"
      " with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

# Storing a list in a Dictionary = Example 2
favorite_languages = {
  'jen': ['python', 'ruby'],
  'sarah':['c'],
  'edward':['ruby','go'],
  'phil':['python','haskell'],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

# A Dictionary in a Dictionary
users = {
  'aeinstein': {
    'first':'albert',
    'last':'einstein',
    'location':'princeton',
  },
  'mcurie': {
    'first':'marie',
    'last':'curie',
    'location':'paris',
  },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

# Example 6-8 Pets:
pet0 = {'type':'cat','owner':'Bob'}
pet1 = {'type':'dog', 'owner':'Tom'}
pet2 = {'type':'dragon', 'owner':'khaleesi'}

pets = [pet0, pet1,  pet2]

for pet in pets:
    print(f"{pet['owner'].title()} has a {pet['type'].title()}")


