# Second function = este o functie care citeste / converteste fisierul csv intr-un dictionar 
#( dictionarul are ca si prima cheie prima coloana din csv si ca valoare are tuple pentru restul coloanelor)

import csv
import os
from function4 import getDictBySubcategory
from csv_file_creation import csv_file_creation

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

path = "/home/skippy/work/python-training/Homework/FinalProject/data.csv"
if os.path.isfile(path):
    data_dictionary = csv_dictionary(path)
 
else:
    print("File does not exist.")


#headere= [_key	link	nutritional_info/Grasimi	nutritional_info/Valoare energetica	nutritional_info/Glucide	nutritional_info/Fibre	nutritional_info/Sodiu	nutritional_info/Proteine	nutritional_info/Grasimi saturate	Ingrediente	Alergeni]
test = []

test = getDictBySubcategory(data_dictionary) 
finalCsv =  csv_file_creation(test)
