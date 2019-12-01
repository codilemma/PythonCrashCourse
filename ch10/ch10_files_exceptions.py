with open('text_files/pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

# Read returns an empty line when it reaches the end of a string.
# Use .rstrip() to remove it
with open('text_files/pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

# U can also use absolute paths
# file_path = '/home/ehmatthes/other_files/text_files/filename.txt'
# with open(file_path) as file_object:

# Reading Line by Line
file_name = 'text_files/pi_digits.txt'
with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())  # use .rstrip() to remove blank line

# Making a list of lines from a file
with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

# Working with a File's Contents
with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()  #concatinate lines into variable

print(pi_string) #print variable
print(len(pi_string)) #print variable character length

# Working with larger files
filename = "text_files/pi_million_digits.txt"

with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))

# Is your Birthday Contained in Pi?
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi! ")
else:
    print("Your birthday does not appear in the first million digits of pi.")

# Using replace
message = "I really like dogs."
new_message = message.replace('dog','cat')
print(new_message)

# Writing to an Empty File
file_name = 'text_files/programming.txt'
with open(file_name, 'w') as file_object:
    file_object.write("I love programming.")

# Writing multiple lines to a File - Overwrites existing file
file_name = 'text_files/programming.txt'
with open(file_name, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

# Append lines to a file.
file_name = 'text_files/programming.txt'
with open(file_name, 'a') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

# Handling Exceptions
# 'print(5/0)' with raise the following exception
#   Traceback (most recent call last):
#    File "division_calculator.py", line 1, in <module>
#      print(5/0)
# ZeroDivisionError: division by zero

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# Using Exceptions to Prevent Crashes
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number =='q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)

# Handling the FileNotFoundError Exception
filename = 'alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")

# Using Split
title = "Alice in Wonderland"
print(title.split())

# Analyzing Text

def count_words(filename):   
    """Count the approximate number of words in a text file""" 
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # or you can write 'pass' to tell python to fail silently
        print(f"Sorry, the file {filename} does not exist.")
    else:
        # Count the approximate number of words in the file.
        words = contents.split() # splits words on the space
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


filename = 'text_files/alice.txt'
count_words(file_name)

# Working with Multiple text files
path = 'text_files/'
files = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
filepaths = [path + f for f in files]
print(filepaths)

for filepath in filepaths:
    print(filepath)
    count_words(filepath)

# Using the count() method to find out how many times
# a word appears in a string.
line = "Row, row, row your boat"
print(line.count('row')) # Returns 2
print(line.lower().count('row')) # Returns 3

# Storing Data - JSON
import json

numbers = [2,3,4,7,11,13]

filename = 'text_files/numbers.json'
# store numbers in a json file
with open(filename, 'w') as f:
    json.dump(numbers, f)
# read the json file to put numbers back into memory
with open(filename) as f:
    numbers2 = json.load(f)
print(numbers2)

# Saving and Reading User-Generated Data
def get_stored_username():
    """Get stored username if availabele."""
    filename = 'text_files/username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        print("There is no username stored")
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name?")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")


