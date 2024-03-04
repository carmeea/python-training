"""
19. Given a tuple, use a range of indexes to print the third, fourth, and fifth item in the tuple​
"""

# my_tuple=()


def values():
    value = int(
        input(
            "How many values should the touple contain?(minimum required number is 5) "
        )
    )
    while value < 5:
        value = int(
            input("Invalid entry. You must enter a value greater or equal than 5: ")
        )
    return int(value)


def enter_values(value):
    my_tuple = ()
    second_tuple = ()
    for i in range(value):
        values = input("Enter value: ")
        second_tuple = (values,)
        my_tuple = my_tuple + second_tuple
    print(my_tuple)
    print("Print the third from tuple", my_tuple[2])
    print("Print the fourth from tuple", my_tuple[3])
    print("Print the fifth from tuple", my_tuple[4])
    return my_tuple


enter_values(values())
