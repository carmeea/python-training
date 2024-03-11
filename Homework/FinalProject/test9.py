import csv

def create_dictionary():
    my_dictionary = {}
    with open('myOutputFile.csv', 'r') as filename:
        file = csv.DictReader(filename)
        my_Tuples = []
        for row in file:
            my_Tuples.append(tuple([row['_key'], row['link']]))
        my_dictionary = dict(my_Tuples)
    # print(my_dictionary["Pufuleti cu sare 45g"])
    # print(my_dictionary.get("Pufuleti cu sare 45g"))
    # print("Pufuleti cu sare 45g" in my_dictionary.keys())
    # print("https://www.mega-image.ro/Dulciuri-si-snacks/Popcorn-covrigei-si-pufuleti/Snacks-uri-si-pufuleti/Pufuleti-cu-sare-45g/p/68656" 
    #     in my_dictionary.values())
    #print(list(my_dictionary.values()))
    # print(len(my_dictionary))
    return my_dictionary

def get_value(search_key, my_dictionary):
    res = []
    for key, val in my_dictionary.items():
        if search_key in key:
            res.append(val)
    print("Values for substring keys : " + str(res))

def get_key(val, my_dictionary):
    for key, value in my_dictionary.items():
        if val == value:
            return key
    return "key doesn't exist"

def search_values(search_value, my_dictionary):
    value = []
    for i in my_dictionary:
        if my_dictionary[i] == search_value:
                value.append(i)
    print("Values for substring values : " + str(value))

get_value("Pufuleti", create_dictionary())

print(get_key("https://www.mega-image.ro/Dulciuri-si-snacks/Popcorn-covrigei-si-pufuleti/Snacks-uri-si-pufuleti/Pufuleti-cu-sare-45g/p/68656", create_dictionary()))

search_values("https://www.mega-image.ro/Dulciuri-si-snacks/Popcorn-covrigei-si-pufuleti/Snacks-uri-si-pufuleti/Pufuleti-cu-sare-45g/p/68656", create_dictionary())