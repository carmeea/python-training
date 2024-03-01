import os
import math

"""
1. Print your current working directory
"""

# get the current working directory
current_working_directory = os.getcwd()

# print output to the console
print(current_working_directory)

"""
2. Create a directory with a file inside it
"""

path = "./aura_folder"

try:
    os.mkdir(path)
    print("Folder %s created!" % path)
except FileExistsError:
    print("Folder %s already exists" % path)

"""
3. Print factorial and square of a number
"""

num = int(input("Please insert your number: \n"))


def factorial(num):
    return math.factorial(num)


def square(num):
    return math.pow(num, 2)


print("Factorial of", num, "is", factorial(num))
print("Square of", num, "is", square(num))


"""
4. Return path of a specific file
"""

my_file = "homework_functions.py"
# print(os.path.abspath(my_file))


def path_of_specific_file(specific_file):
    return os.path.abspath(specific_file)


print(f"Path of your file is:", path_of_specific_file(my_file))

"""
5. Print random integer between 0 and 5
"""
from random import randrange

print(randrange(5))

"""
6. Print current datetime
"""
from datetime import datetime

current_datetime = datetime.now()

print("Now =", current_datetime)

"""
7. Print current time
"""
print(current_datetime.time())
print(current_datetime.date())

"""
8. Converts a number of seconds to a date
"""

print(datetime.fromtimestamp(1709312191).strftime("%A, %B %d, %Y %H:%M:%S"))

from datetime import timedelta

sec = int(input("Insert the number of seconds \n"))
print("Time in Seconds:", sec)

td = timedelta(seconds=sec)
print("Time in hh:mm:ss:", td)


"""
9. Print the value of pi
"""
print(math.pi)

"""
10. Create your own module and import it in another python file
"""

import calculations

num = 120

print("Factorial of", num, "is", calculations.factorial(num))
print("Square of", num, "is", calculations.square(num))
