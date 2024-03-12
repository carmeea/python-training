# Second function = este o functie care citeste / converteste fisierul csv intr-un dictionar 
#( dictionarul are ca si prima cheie prima coloana din csv si ca valoare are tuple pentru restul coloanelor)

import csv
import os
from function3 import getSubcategory

def csv_dictionary(file_path):
    product_dictionary = {}
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        for column in reader: 
            primary_key = column[0]
            values_tuple = tuple(column[1:])
            product_dictionary[primary_key] = values_tuple
    return product_dictionary

path = "/home/dan/work/python-training/Homework/FinalProject/data.csv"
if os.path.isfile(path):
    data_dictionary = csv_dictionary(path)
    print(data_dictionary)
else:
    print("File does not exist.")
def getSubcategory(dictionary):
    subcategoryList = []
    for val in (i[0] for i in dictionary.values()):
        subcategory = val.split('/')[4]
        subcategoryList.append(subcategory)
    return subcategoryList
test = []
test = getSubcategory(data_dictionary) 
print(test)
 