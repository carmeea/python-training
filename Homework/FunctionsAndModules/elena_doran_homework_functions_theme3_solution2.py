"""
3. Create a function with 3 arguments and return average only if is greater than 0
"""

import statistics


def enter_numbers():
    number1 = input("Enter first number: ")
    number2 = input("Enter second number: ")
    number3 = input("Enter third number: ")
    return int(number1), int(number2), int(number3)


def return_average():
    try:
        average = statistics.mean(enter_numbers())
        if average > 0:
            print("Average is:", average)
        else:
            print("Wrong numbers!")
    except ValueError as e:
        print("You did not enter a number")
        return None


return_average()
