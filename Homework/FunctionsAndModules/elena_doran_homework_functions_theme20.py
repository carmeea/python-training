"""
20. Given a dictionary, add a new key/value to the dictionary and print each item
"""

my_Dictionary = {}


def values():
    key_value = int(input("How many key/value should the dictionary contain? "))
    return int(key_value)


def update_dictionary(key_value):
    for i in range(key_value):
        key = input("Enter key: ")
        value = input("Enter value: ")
        my_Dictionary.update({key: value})
    print(my_Dictionary)
    print("Key-Value Pairs:", my_Dictionary.items())
    print("Keys:", my_Dictionary.keys())
    print("Values:", my_Dictionary.values())
    for key, value in my_Dictionary.items():
        print(key, ":", value)
    return my_Dictionary


update_dictionary(values())
