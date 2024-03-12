import csv
import pandas as pd
import pprint

# subcategory = input("Enter a subcategory for the search: ")

subcategoryDict = {}
base_category = "Dulciuri-si-snacks"
with open("data.csv", "r") as datafile:
    reader=csv.DictReader(datafile)
    #csvwriter = csv.writer(newfile)

    for data in reader:
        # if subcategory.lower() in data[1].lower():
        #     csvwriter.writerow(data)
        #     print("File created successfully")
        #     print("File name: Filtered file.csv")
        # else:
        #     print("Subcategory not found")
        #     break
        split_link = data["link"].split("/")
        index = split_link.index(base_category) + 1
        #subcategoryDict[split_link[index]] = data
        subcategory = split_link[index]
        if subcategory in subcategoryDict:
            subcategoryDict[subcategory].append(data)
        else:
            subcategoryDict[subcategory] = [data]
    #pprint.pprint(subcategoryDict)
    print(subcategoryDict.keys())
        

    