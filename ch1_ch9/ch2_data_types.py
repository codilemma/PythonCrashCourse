
# Changing Case in a String with Methods
name = "ada lovelace"
print(name.title())

name2 = "Ada Lovelace"
print(name.upper())
print(name.lower())

# Using Variables in Strings
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"   #f-strings, f specifies format
print(full_name)
print(f"Hello, {full_name.title()}!")
message = f"\tHello, {full_name.title()}!"
print(message)

# Stripping whitespace from right side
favorite_language = ' python '
print(favorite_language.rstrip())

# Stripping whitespace from left side
print(favorite_language.lstrip())

# Stripping whitespace from both sides
print(favorite_language.strip())

# You can use underscores in numbers! only available in python 3.6
universe_age = 14_000_000_000

# Multiple Assignment
x, y, z = 0, 0, 0

# Python does not have a constant variable.  Use ALL CAPS to specify constant for readability
MAX_CONNECTIONS = 5000
