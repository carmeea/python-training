"""
1. Print your current working directory
"""

import os

current_directory = os.getcwd()
print("The current working directory is:", current_directory)


"""
2. Create a directory with a file inside it
"""

import os

directory_path = "/home/cosmin/work/python-training/Homework/FunctionsAndModules"
directory_name = "homework_directory"
file_name = "homework_file.txt"

os.mkdir(os.path.join(directory_path, directory_name))

file_path = os.path.join(directory_path, directory_name, file_name)

with open(file_path, 'w'):
    pass


"""
3. Print factorial and square of a number
"""

import math

n = 5

factorial = math.factorial(n)
square = math.pow(n, 2)

print(f"Factorial of {n} is: {factorial}")
print(f"Square of {n} is: {square}")


"""
4. Return path of a specific file
"""

import os

print("The path of the given file is:", os.path.abspath("homework_modules.py"))


"""
5. Print random integer between 0 and 5
"""

import random

rand_int = random.randint(0, 5)
print(rand_int)


"""
6. Print current datetime
"""

from datetime import datetime

current_datetime = datetime.now()
print(current_datetime)


"""
7. Print current time
"""

from datetime import datetime

current_datetime = datetime.now()
current_time = current_datetime.time()
print(current_time)


"""
8. Converts a number of seconds to a date
"""

from datetime import datetime

timestamp = 1709640084
date = datetime.fromtimestamp(timestamp)
print(date)


"""
9. Print the value of pi
"""

import math

print(math.pi)


"""
10. Create your own module and import it in another python file
"""

import my_module

my_module.greet("Jack")