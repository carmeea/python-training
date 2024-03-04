"""
17. Get the largest and the smallest number from a list
"""

list = []


def numbers():
    number = input("How many numbers should the list contain? ")
    return int(number)


def enter_numbers(number):
    for i in range(number):
        numbers = int(input("Enter number: "))
        list.append(numbers)
    print(list)
    return list


def max_min(list):
    print("Maximum element in the list is :", max(list))
    print("Maximum element in the list is :", min(list))


max_min(enter_numbers(numbers()))
