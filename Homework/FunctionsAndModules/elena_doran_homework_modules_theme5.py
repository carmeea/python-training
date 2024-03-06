"""
5. Print random integer between 0 and 5
"""

import random


def print_random(number):
    print("x = ", random.randrange(number))
    print("y = ", random.randrange(0, number))


print_random(6)
