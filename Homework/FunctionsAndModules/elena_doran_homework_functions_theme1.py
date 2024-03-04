"""
1. Create a function which prints first 10 natural numbers
"""


def print_numbers1(number):
    i = 1
    while i < (number + 1):
        print(i)
        i += 1


def print_numbers2(number):
    for i in range(1, number + 1):
        print(i)


print_numbers1(10)
print_numbers2(10)
