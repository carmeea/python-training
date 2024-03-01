import math

"""
3. Print factorial and square of a number
"""

num = 5


def factorial(num):
    return math.factorial(num)


def square(num):
    return math.pow(num, 2)


print("Factorial of", num, "is", factorial(num))
print("Square of", num, "is", square(num))
