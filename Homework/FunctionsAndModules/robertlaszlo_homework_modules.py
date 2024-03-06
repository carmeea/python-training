"""
1. Print your current working directory
"""

import os

current_directory = os.getcwd()
print(current_directory)

"""
2. Create a directory with a file inside it
"""

def create_dir_with_file(dir_name, file_name):
    os.makedirs(dir_name, exist_ok=True)

    file_path= os.path.join(dir_name, file_name)
    with open(file_path, 'w') as file:
        file.write("This is a test file.")

    print("Directory with file created")

create_dir_with_file("New text file directory", "test_file.txt")

"""
3. Print factorial and square of a number
"""

def factorical_square_of_one_number(number):
    factorial = 1
    square = number ** 2

    for i in range(1, number+1):
        factorial *= i
    
    return factorial, square

factorial, square = factorical_square_of_one_number(5)
print(factorial, square)

"""
4. Return path of a specific file
"""

import os

def find_and_return_path(dir, filename):
    for root, dirs, files in os.walk(dir):
        if filename in files:
            return os.path.join(root, filename)
    return None

file_path = find_and_return_path('//home/rotestbert/work/python-training/Homework/FunctionsAndModules/New text file directory', 'test_file.txt')
if file_path:
    print("Found here: ", file_path)
else:
    print("File not found")

"""
5. Print random integer between 0 and 5
"""

import random

def print_random_int_number():
    random_number = random.randint(0, 5)
    print("Lucky number is: ", random_number)

print_random_int_number()

"""
6. Print current datetime
"""

import datetime

def print_curent_date_time():
    current_time = datetime.datetime.now()
    print("Current date and time is: ", current_time)

print_curent_date_time()

"""
7. Print current time
"""

import time

def print_curent_time():
    current_time = time.strftime("%H:%M", time.localtime())
    print("Current time is: ", current_time)

print_curent_time()

"""
8. Converts a number of seconds to a date
"""

from datetime import datetime, timedelta

def convert_epoch_to_date(seconds):
    base_date = datetime(1970,1,1)
    date_after_conversion = base_date + timedelta(seconds=seconds)
    return date_after_conversion

date = convert_epoch_to_date(1709756883)
print(date)

"""
9. Print the value of pi
"""

import math

print(math.pi)

"""
10. Create your own module and import it in another python file
"""

import robertlaszlo_module

robertlaszlo_module.proof_of_my_own_module()
