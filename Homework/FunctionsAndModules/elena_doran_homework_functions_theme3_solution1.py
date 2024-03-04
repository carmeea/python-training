"""
3. Create a function with 3 arguments and return average only if is greater than 0
"""

import statistics


def enter_numbers():
    number1 = input("Enter first number: ")
    number2 = input("Enter second number: ")
    number3 = input("Enter third number: ")
    return int(number1), int(number2), int(number3)


def get_sum(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum


def get_lenght(numbers):
    list = []
    for number in numbers:
        list.append(number)
    lenght = len(list)
    return lenght


def get_average(numbers):
    average = get_sum(numbers) / get_lenght(numbers)
    return average


def return_average(average):
    if average > 0:
        print("Average is:", average)
    else:
        print("Wrong numbers!")


return_average(get_average(enter_numbers()))
