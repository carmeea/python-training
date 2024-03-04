"""
9. Define a function that checks if a given number is a prime number​
"""

import prime


def check_number(number):
    if prime.isPrime(number) is True:
        print("The number", number, "is prime.")
    else:
        print("The number", number, "is not prime.")


check_number(7)
