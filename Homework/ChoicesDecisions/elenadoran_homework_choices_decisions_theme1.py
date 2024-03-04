"""
1. Write a program that finds all numbers which are divisible by 7 and multiples of 5,
between 1500 and 2700 (both included). 
Then accept a number from the user and verify if it is part of the found list numbers.
Hint: use methods range(), input(), append(), try-except
"""


def enter_start_range():
    start_range = input("Enter start range ")
    return int(start_range)


def enter_end_range():
    end_range = input("Enter end range ")
    return int(end_range)


def get_list(start, end):
    found_list = []

    for i in range(start, end + 1):
        if i % 7 == 0 and i % 5 == 0:
            print(i, "is divisible by 7 and multiple of 5")
            found_list.append(i)

    print("The found list is: ", found_list)
    return found_list


def number(found_list):
    number = input("Enter a number: ")
    try:
        i = int(number)
        found_list = get_list(enter_start_range(), enter_end_range())
        if i in found_list:
            print("The number is part of the found list numbers")
        else:
            print("The number is not part of the found list numbers")
    except ValueError as e:
        print("You did not enter a number")


# get_list(enter_start_range(), enter_end_range())
number(get_list)
