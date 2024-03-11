import csv

def create_dictionary():
    my_dictionary = {}
    with open('myOutputFile.csv', 'r') as filename:
        file = csv.DictReader(filename)
        my_Tuples = []
        for row in file:
            my_Tuples.append(tuple([row['_key'], row['link']]))
        my_dictionary = dict(my_Tuples)
    print(my_dictionary["Pufuleti cu sare 45g"])
    print(my_dictionary.get("Pufuleti cu sare 45g"))
    print("Pufuleti cu sare 45g" in my_dictionary.keys())
    print("https://www.mega-image.ro/Dulciuri-si-snacks/Popcorn-covrigei-si-pufuleti/Snacks-uri-si-pufuleti/Pufuleti-cu-sare-45g/p/68656" 
        in my_dictionary.values())
    print(len(my_dictionary))
    search_key = "Pufuleti"
    res = []
    for key, val in my_dictionary.items():
        if search_key in key:
            res.append(val)

    print("Values for substring keys : " + str(res))

    return my_dictionary

create_dictionary()

