"""
1. Print your current working directory
"""
import os

def print_cwd():
    print("Current working directory:", os.getcwd())

print_cwd()


"""
2. Create a directory with a file inside it
"""

"""
3. Print factorial and square of a number
"""

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    print("Factorial of", n, ":", result)

def square(n):
    result = n ** 2
    print("Square of", n, ":", result)

number = 5

factorial(number)  
square(number)     




"""
4. Return path of a specific file
"""

"""
5. Print random integer between 0 and 5
"""
import random

def print_random_integer():
    random_int = random.randint(0, 5)
    print("Random integer between 0 and 5:", random_int)

print_random_integer()



"""
6. Print current datetime
"""
from datetime import datetime

def print_current_datetime():
    current_datetime = datetime.now()
    print("Current date and time:", current_datetime)

print_current_datetime()


"""
7. Print current time
"""
from datetime import datetime

def print_current_time():
    current_time = datetime.now().time()
    print("Current time:", current_time)

print_current_time()



"""
8. Converts a number of seconds to a date
"""

"""
9. Print the value of pi
"""

import math

def print_pi_value():
    print("The value of pi:", math.pi)

print_pi_value()

"""
10. Create your own module and import it in another python file
"""
