# FUNCTIONS AND MODULES

"""
Functions are pre-=written codes that perfom a certain task (have a well defined scope)
Parameters - some functions require to pass data for them to perform the the task, called parameters.
Examples of predefined functions that require parameters, like print(), sum(), etc.

Structure
def functionaName(parameters):
    [...] #code to execute task
    return [expression]
-if your function does not need to return any value, you can omit return. Alternatively you can write
return or return None
"""

# DEFINE A FUNCTION


# Determin if a given number is prime
def checkIfPrime(numberToCheck):
    # Loop to devide numbertoCheck by all numbers from 2 to numbertoCheck-1
    for x in range(2, numberToCheck):
        # if remaider is zero, return false and exit function
        if numberToCheck % x == 0:
            return False
    return True


# Calling the function
answer = checkIfPrime(13)
print(answer)

# VARIABLE SCOPE
# Global and Local variables
"""
Variables defined inside are treated differently from variables defined outside.
Variable declared inside a function is only accesisible inside the function (local variables).
Variables defined outside functions are accessible anywhere in the program (global variables).
"""
message1 = "Global variable"


def myFunction():
    print("\nInside the function")
    print(message1)
    message2 = "Local variable"
    print(message2)


myFunction()
print(message1)
# print(message2)  # NameError: name 'message2' is not defined.


"""
Another concept to understand about variable scope:
If a local variable shares the same name as a global variable, the code inside the function is
accessing the local variable. The code outside the the function is accesing the global variable.
"""
message1 = "This is a Global variable"


def myFunction2():
    message1 = "This is a Local variable"
    print("\nInside the function")
    print(message1)


myFunction2()
print("\nOutside the function")
print(message1)

# Non-Local variables
"""
Nonlocal variables refer to all those variables that are declared within nested functions. 
The local scope of a nonlocal variable is not defined.
https://www.w3schools.com/python/ref_keyword_nonlocal.asp
https://en.wikipedia.org/wiki/Non-local_variable
"""

# Python Keyword Argument


# Arguments are assignet based on the name of the arguments
def display_info(first_name, last_name):
    print("First Name:", first_name)
    print("Last Name:", last_name)


display_info(last_name="Ionela", first_name="Crisan")

# Arbitrary arguments
# (*) - allow to pass a varying number of values during function call


# find sum of multiple numbers
def calc_sum(*numbers):
    result = 0
    for num in numbers:
        result = result + num
    print("Sum = ", result)


# function call with 3 arguments
calc_sum(1, 2, 3)
# function call with 2 arguments
calc_sum(4, 9)


# Python Recursive Function
# Factorial number - Factorial of 6 -> 1*2*3*4*5*6 = 720
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


num = 3
print("The factorial of", num, "is", factorial(num))  # The factorial of 3 is 6
"""
factorial(3)          # 1st call with 3
3 * factorial(2)      # 2nd call with 2
3 * 2 * factorial(1)  # 3rd call with 1
3 * 2 * 1             # return from 3rd call as number=1
3 * 2                 # return from 2nd call
6                     # return from 1st call
"""


# Create a recursive function to calculate the sum of numbers from 0 to 10
def addition(num):
    if num:
        print(num)
        # call same function by reducing number by 1
        return num + addition(num - 1)
    else:
        return 0


res = addition(10)
print(res)  # 55


# IMPORTING MODULES
"""
Python comes with many built-in functions. These functions are grouped and saved in files known as modules.
-To use these functions, we have to import the modules first. Syntax is import moduleName. 
 Example: import random -> to use randrange() functio n from random module. To use: random.randrange(1, 10)
-You can abreviate the name of the module: import random as r -> r.randrange(1, 10)
-You can also import only specific function from a module: from moduleName import functionName1, functionName2,... .
Example: from random import randrange, randint -> to use the function now simply call randrange(1, 10) without module name.
"""
from datetime import datetime

now = datetime.now()  # current date and time
# converting datetime object to different string formats
year = now.strftime("%Y")
print("year:", year)
month = now.strftime("%m")
print("month:", month)
day = now.strftime("%d")
print("day:", day)
time = now.strftime("%H:%M:%S")
print("time:", time)
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:", date_time)

# -----

date_string1 = "29 February, 2024"
print("date_string =", date_string1)
print("type of date_string =", type(date_string1))

# creating a datetime object from give string
# string needs to be in format accepted, %d -day of the month, %B -month's name in full, %Y - year in 4 digits
date_object = datetime.strptime(date_string1, "%d %B, %Y")
print("date_object =", date_object)
print("type of date_object =", type(date_object))
dt_string = "12/11/2018 09:15:32"

# Considering date is in dd/mm/yyyy format
dt_object1 = datetime.strptime(dt_string, "%d/%m/%Y %H:%M:%S")
print("dt_object1 =", dt_object1)

# Considering date is in mm/dd/yyyy format
dt_object2 = datetime.strptime(dt_string, "%m/%d/%Y %H:%M:%S")
print("dt_object2 =", dt_object2)

# -----

import math

square_root = math.sqrt(4)  # returns the square root of a number
print("Square Root of 4 is", square_root)  # Square Root of 4 is 2.0
power = pow(2, 3)  # returns the power of a number
print("2 to the power 3 is", power)  # 2 to the power 3 is 8

# import only pi from math module
from math import pi

print(pi)

# import all names from the standard module math
from math import *

print("The value of pi is", pi)

# CREATING A MODULE
"""
Besides importing built-in modules, we can create our own modules. This is helpful if you want to reuse some functions.
How to create a module -> View prime.py
"""
import prime

n = 13
answer = prime.isPrime(n)
print("Number ", n, "is prime: ", answer)  # Number  13 is prime:  True
