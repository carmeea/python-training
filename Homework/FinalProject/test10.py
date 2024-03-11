import csv

def create_dictionary():
    my_dictionary = {}
    with open('myOutputFile.csv', 'r') as filename:
        file = csv.DictReader(filename)
        my_Tuples = []
        for row in file:
            my_Tuples.append(tuple([row['_key'], row['link']]))
        my_dictionary = dict(my_Tuples)
    return my_dictionary

def return_value_dictionary(search_key, my_dictionary):
    values_dictionary = []
    for key, value in my_dictionary.items():
        if search_key in key:
            values_dictionary.append(value)
    print("Values for substring keys : " + str(values_dictionary))

def return_key_dictionary(search_value, my_dictionary):
    key_dictionary = []
    for value in my_dictionary:
        if my_dictionary[value] == search_value:
                key_dictionary.append(value)
    print("Values for substring values : " + str(key_dictionary))

return_value_dictionary("Pufuleti", create_dictionary())
return_key_dictionary("https://www.mega-image.ro/Dulciuri-si-snacks/Popcorn-covrigei-si-pufuleti/Snacks-uri-si-pufuleti/Pufuleti-cu-sare-45g/p/68656", create_dictionary())