import csv

"""
enter_subcategory() function  was created with the scope for asking the user to enter the number of subcategories and subcategory type.
A list is created and will contain all subcategory types.
casefold() method returns a string where all the characters are lower case.
"""


def enter_subcategory():
    list = []
    number = int(input("After how many subcategories would you like to search "))
    for i in range(number):
        subcategory = input(f"Enter {i+1} subcategory: ")
        list.append(subcategory.casefold())
    print(list)
    return list


"""
create_dictionary() function is used to pass keys as tuple inside a dictionary.
First open the .csv file and read data from it.
Second create a tuple by taking from .csv file only the '_key' and 'link' columns .
For 'link' column it was used row["link"].split("/")[4]).replace("-", " ").casefold() 
Example: https://www.mega-image.ro/Dulciuri-si-snacks/Dropsuri-guma-si-jeleuri/Drajeuri/Bomboane-de-ciocolata-crispy-cu-miez-crocant-77g/p/34630 
        -> we get 'dropsuri guma si jeleuri'
Third a dictionary was created from tuple with data pairs key-value: ('_key': 'link').
"""
#check after alphanumeric - alpha()

def create_dictionary():
    my_dictionary = {}
    with open("data.csv", "r") as filename:
        file = csv.DictReader(filename)
        my_Tuples = []
        for row in file:
            my_Tuples.append(
                tuple(
                    [
                        row["_key"],
                        (row["link"].split("/")[4]).replace("-", " ").casefold(),
                    ]
                )
            )
        my_dictionary = dict(my_Tuples)
    return my_dictionary


"""
return_key_dictionary() function is used to search into dictionary created with create_dictionary() function 
by all the elements from list created with enter_subcategory() function.
If the element is found in the dictionary, then a new file 'myOutputFile-element_name.csv' is created 
with the corresponding values from dictionary. For each element found a new csv file is created.
If the element is not found in the dictionary, then throw an exception.
"""


def return_key_dictionary(list, my_dictionary):
    for element in list:
        matches = []
        for value in my_dictionary:
            if element in my_dictionary[value]:
                matches.append(value)
        try:
            if len(matches) > 0:
                print(
                    f"The products found for given subcategory {element} are:",
                    str(matches),
                )
                outputFile = open(f"myOutputFile-{element}.csv", "wt")
                outputFile.write("\n".join(matches))
                outputFile.close()
            else:
                raise ValueError(f"No file created for given subcategory {element}!")
        except ValueError as e:
            print(e)


return_key_dictionary(enter_subcategory(), create_dictionary())
