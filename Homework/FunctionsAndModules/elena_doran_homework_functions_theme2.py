"""
2. Create a function which prints sum of all numbers from 1 to a given number (e.g. print sum of all numbers from 1 to 5)
"""


def enter_number():
    number = input("Enter a number: ")
    return int(number)


def sum_numbers(number):
    total = 0
    for i in range(number + 1):
        total += i
    print(total)


sum_numbers(enter_number())
