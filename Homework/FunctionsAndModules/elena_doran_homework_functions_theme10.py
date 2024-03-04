"""
10. Define a function which prints all the numbers between 1000 and 2000 which are divisible by 7 but are not a multiple of 5
"""


def enter_start_range():
    start_range = input("Enter start range ")
    return int(start_range)


def enter_end_range():
    end_range = input("Enter end range ")
    return int(end_range)


def get_list(start, end):
    found_list = []

    for i in range(start, end):
        if i % 7 == 0 and i % 5 != 0:
            print(i, "is divisible by 7 and not multiple of 5")
            found_list.append(i)

    print("The found list is: ", found_list)
    return found_list


get_list(enter_start_range(), enter_end_range())
