import csv

new_dictionary = {}

with open('myOutputFile.csv', 'r') as filename:
    file = csv.DictReader(filename)
    myTuples = []
    for row in file:
        myTuples.append(tuple([row['_key'], row['link']]))
    new_dictionary = dict(myTuples)
#print(new_dictionary)
print(new_dictionary["Pufuleti cu sare 45g"])
print(new_dictionary.get("Pufuleti cu sare 45g"))
print("Pufuleti cu sare 45g" in new_dictionary.keys())
print("https://www.mega-image.ro/Dulciuri-si-snacks/Popcorn-covrigei-si-pufuleti/Snacks-uri-si-pufuleti/Pufuleti-cu-sare-45g/p/68656" 
      in new_dictionary.values())
# print(result.keys())
# print(result.values())
print(len(new_dictionary))