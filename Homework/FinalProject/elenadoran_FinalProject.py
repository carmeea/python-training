import csv


def enter_subcategory():
    list = []
    number = int(input("After how many subcategories would you like to search "))
    for i in range(number):
        subcategory = input(f"Enter {i+1} subcategory: ")
        list.append(subcategory.casefold())
    print(list)
    return list


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
