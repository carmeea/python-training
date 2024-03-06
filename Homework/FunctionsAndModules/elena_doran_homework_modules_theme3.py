"""
3. Print factorial and square of a number
"""

import factorial, math


def print_factorial(number):
    print("The factorial of", number, "is", factorial.calculate_factorial(number))


def print_square(number):
    print("The square of", number, "is", math.sqrt(number))


print_factorial(4)
print_square(4)
