"""
Given the data.csv file, find all products for a subcategory.

1.Find all products for a subcategory given by the user and export them (write) to another CSV file. 

2.Subcategory will be given as input from user.
ex: Category=Dulciuri si Snacks, Subcategoy=Napolitane biscuiti si prajituri, Ciocolata, Chipsuri
Subcategory search should not be case sesitive. For example user can give as input ->NaPOLItane Biscuiti SI prajiturI

3.If subcategory is not found throw an error back to the user and do not create the file.

4.If products are found, notify user that file was created succesfully, specify also the file name.

Note: Apply concepts from previous lessons (data types,  loops, exception handling, files management, functions, etc)
"""

import csv
import sys
import os

file_path = "data.csv"


# functie in care se face split la url-uri dupa "/"
def url_extract(path):
    return path.split("/")


# parsare url_uri
def parssed_urls(list_of_urls):
    splitted_url = [url_extract(url) for url in list_of_urls]
    return splitted_url


# extract subcategorii din nested list (dupa indexul 4)
def extract_subcategory(lst):
    return [item[4] for item in lst]


def extract_unique_subcategory_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            # read csv file and extract the urls( second column) in a list
            csv_reader = csv.reader(file)
            url_lst = [row[1] for row in csv_reader]
            # remove column header which is string "link"
            url_lst.pop(0)
            prsd_url = parssed_urls(url_lst)
            all_subcategories = extract_subcategory(prsd_url)
            # print(all_subcategories)
            # iterate the subcategories list obtained above and remove duplicates
            unique_subcategories = []
            for item in all_subcategories:
                if item not in unique_subcategories:
                    unique_subcategories.append(item)
            return unique_subcategories

    except FileNotFoundError:
        print(f"File {file} not found.  Aborting")
        sys.exit(1)
    except OSError:
        print(f"OS error occurred trying to open {file}")
        sys.exit(1)
    except Exception as err:
        print(f"Unexpected error opening {file} is", repr(err))
        sys.exit(1)


# print(extract_unique_subcategory_from_file(file_path))


# in caz ca ne razgandim si nu mai dam user input cu numere
def subcategory_lower():
    """Sets the elements of the list to lower case"""
    new_products = extract_unique_subcategory_from_file(file_path)
    product_subcategory = [i.lower() for i in new_products]
    return product_subcategory


def replace_chars(lst):
    new_lst = [x.replace("-", " ") for x in lst]
    return new_lst


subcategories_lower = subcategory_lower()
subcat = replace_chars(subcategories_lower)


def find_element(csv_file, element):
    with open(csv_file, "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if element in row:
                return row
    return None


while True:
    try:
        subcategory = input("Enter one of the subcategories: " + str(subcat))
        subcategory = subcategory.lower()
        if subcategory in subcat:
            print("File was created")
            break
        else:
            print("File was no created. Try again!")
            break
    except ValueError as e:
        print(str(e))
