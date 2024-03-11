import csv
import urllib.parse

def create_dictionary():
    my_dictionary = {}
    with open('myOutputFile.csv', 'r') as filename:
        file = csv.DictReader(filename)
        my_Tuples = []
        for row in file:
            my_Tuples.append(tuple([row['_key'], (row['link'].split("/")[4]).replace("-", " ")]))
        my_dictionary = dict(my_Tuples)
    return my_dictionary

def get_key(search_value, my_dictionary):
    key_dictionary = []
    for key, value in my_dictionary.items():
        if search_value.find(value):
            key_dictionary.append(key)
    #print("Values for substring keys : " + str(key_dictionary))

    if len(key_dictionary) > 0:
        print("The key for the value", search_value, "is", key_dictionary[0])
    else:
        print("Value not found in dictionary")

#print(create_dictionary())
get_key("Popcorn covrigei si pufuleti", create_dictionary())


#get_key("https://www.mega-image.ro/Dulciuri-si-snacks/Popcorn-covrigei-si-pufuleti/Snacks-uri-si-pufuleti/Pufuleti-cu-sare-45g/p/68656", create_dictionary())


# test_str = "https://www.mega-image.ro/Dulciuri-si-snacks/Popcorn-covrigei-si-pufuleti/Snacks-uri-si-pufuleti/Pufuleti-cu-sare-45g/p/68656"
# print("The original string is : " + str(test_str))
# res = test_str.split('/')
# print(res)