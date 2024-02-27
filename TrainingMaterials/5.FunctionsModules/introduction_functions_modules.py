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

# IMPORTING MODULES
"""
Python comes with many built-in functions. These functions are grouped and saved in files known as modules.
-To use these functions, we have to import the modules first. Syntax is import moduleName. 
 Example: import random -> to use randrange() functio n from random module. To use: random.randrange(1, 10)
-You can abreviate the name of the module: import random as r -> r.randrange(1, 10)
-You can also import only specific function from a module: from moduleName import functionName1, functionName2,... .
Example: from random import randrange, randint -> to use the function now simply call randrange(1, 10) without module name.
"""

# CREATING A MODULE
"""
Besides importing built-in modules, we can create our own modules. This is helpful if you want to reuse some functions.
How to create a module -> View prime.py
"""
import prime

n = 13
answer = prime.isPrime(n)
print("Number ", n, "is prime: ", answer)  # Number  13 is prime:  True
