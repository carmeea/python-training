"""
8. Define a function which ask the user for a number and print “Even” if the number is even or “Odd” if the number is odd
"""

import evenOdd


def enter_number():
    number = input("Enter first number: ")
    return int(number)


evenOdd.checkEvenOdd(enter_number())
