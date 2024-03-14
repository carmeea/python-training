import csv
import pandas as pd

#create a dictionary with the subcategories as keys and the values are lists of dictionaries
subcategoryDict = {}
#create a base category to search for
base_category = "Dulciuri-si-snacks"

#open the file and read the data
with open("data.csv", "r") as datafile:
    reader=csv.DictReader(datafile)

#iterate through the data and create a dictionary with the subcategories as keys and the values are lists of dictionaries
    for data in reader:
        #split the link to get the subcategory
        split_link = data["link"].split("/")
        #get the index of the subcategory
        index = split_link.index(base_category) + 1
        #store the subcategory in a variable
        subcategory = split_link[index]
        #if the subcategory is already in the dictionary, append the data to the list
        #if not, create a new key with the subcategory and the value is a list with the data
        if subcategory in subcategoryDict:
            subcategoryDict[subcategory].append(data)
        else:
            subcategoryDict[subcategory] = [data]
    
    #print the subcategories that can be searched
    print(f"Subcategoriile pe care le puteti cauta sunt: {subcategoryDict.keys()}")
    
    subcategory = input("Enter a subcategory for the search: ")
    
    #Key serch in subcategoryDict in a case-insensitive way
    #next function returns the first value that matches the condition
    #matching_key will return None if no key is found
    matching_key = next((key for key in subcategoryDict.keys() if key.lower() == subcategory.lower()), None)

    #if the key is found, create a file with the name of the key and write the data in the file
    if matching_key:
        print(f"Subcategory {matching_key} found in the database")
        print(f"File was created successfully and the name of the file is {matching_key}.csv")
        #create a dataframe with the data
        df = pd.DataFrame(subcategoryDict[matching_key])
        #write the dataframe in a csv file
        df.to_csv(f"{matching_key}.csv", index=False)
    #if the key is not found, print a message and do not create a file
    else:
        print(f"Subcategory {matching_key} not found in the file")
        print(f"No file was created")