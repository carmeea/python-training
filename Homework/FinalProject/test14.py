import csv

def create_dictionary():
    my_dictionary = {}
    with open('myOutputFile.csv', 'r') as filename:
        file = csv.DictReader(filename)
        my_Tuples = []
        for row in file:
            my_Tuples.append(tuple([row['_key'], (row['link'].split("/")[4]).replace("-", " ")]))
        my_dictionary = dict(my_Tuples)
    return my_dictionary

def return_key_dictionary(search_value, my_dictionary):
    key_dictionary = []
    for value in my_dictionary:
        #if my_dictionary[value] == search_value:
        if search_value in my_dictionary[value]:
                key_dictionary.append(value)
    print("Values for substring values : " + str(key_dictionary))


#print(create_dictionary())
return_key_dictionary("biscuiti", create_dictionary())

#get_key("https://www.mega-image.ro/Dulciuri-si-snacks/Popcorn-covrigei-si-pufuleti/Snacks-uri-si-pufuleti/Pufuleti-cu-sare-45g/p/68656", create_dictionary())