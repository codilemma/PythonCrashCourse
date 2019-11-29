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

