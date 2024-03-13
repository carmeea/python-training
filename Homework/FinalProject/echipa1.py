import csv
import pprint
import pandas as pd

subcategoryDict = {}
base_category = "Dulciuri-si-snacks"
with open("data.csv", "r") as datafile:
    reader=csv.DictReader(datafile)
    
    for data in reader: 
        split_link = data["link"].split("/")
        index = split_link.index(base_category) + 1
        #subcategoryDict[split_link[index]] = data
        subcategory = split_link[index]
        if subcategory in subcategoryDict:
            subcategoryDict[subcategory].append(data)
        else:
            subcategoryDict[subcategory] = [data]
    #pprint.pprint(subcategoryDict)
    print(f"Subcategoriile pe care le puteti cauta sunt: {subcategoryDict.keys()}")
    
    subcategory = input("Enter a subcategory for the search: ")
    matching_key = next((key for key in subcategoryDict.keys() if key.lower() == subcategory.lower()), None)

    if matching_key:
        print(f"Subcategory {matching_key} found in the database")
        print(f"File was created successfully and the name of the file is {matching_key}.csv")
        df = pd.DataFrame(subcategoryDict[matching_key])
        df.to_csv(f"{matching_key}.csv", index=False)
    else:
        print(f"Subcategory {matching_key} not found in the file")
        print(f"No file was created")