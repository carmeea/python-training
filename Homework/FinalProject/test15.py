import csv

list = []

def enter_subcategory():
    number = int(input("After how many subcategories would you like to search "))
    for i in range(number):
        subcategory = input(f"Enter {i+1} subcategory: ")
        list.append(subcategory.casefold())
    print(list)
    return list


def create_dictionary():
    my_dictionary = {}
    with open('myOutputFile.csv', 'r') as filename:
        file = csv.DictReader(filename)
        my_Tuples = []
        for row in file:
            my_Tuples.append(tuple([row['_key'], (row['link'].split("/")[4]).replace("-", " ").casefold()]))
        my_dictionary = dict(my_Tuples)
    return my_dictionary

def return_key_dictionary(list, my_dictionary):
    key_dictionary = []
    for value in my_dictionary:
        for element in list:
            if element in my_dictionary[value]:
                 key_dictionary.append(value)


    for element in list:
        if len(key_dictionary) > 0:
                print(f"The products found for given subcategory {element} are:", str(key_dictionary))
        else:
                print(f"No product found for given subcategory {element}!")


return_key_dictionary(enter_subcategory(), create_dictionary())