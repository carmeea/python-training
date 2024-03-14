# process_user_input = solve the user input for key sensitive and return the value (ia inputul , il verifica/ modifica si il returneaza ca o valoare care se va folosi in urmatoarea functie ca si argument)
# csv_dictionary = este o functie care citeste / converteste fisierul csv intr-un dictionar ( dictionarul are ca si prima cheie prima coloana din csv si ca valoare are tuple pentru restul coloanelor)
# getDictBySubcategory =  functie care sa spliteze linkul
#                         sa parcurga toate linkurile in dictionarul returnat de functia de mai sus
#                         compara input user cu lista de subcategorii
#                         returneaza un dictionar cu subcategoria introdusa de user
# csv_file_creation =  sa creeze un file csv nou cu produsele aferente sau sa returneze eroare daca inputul e gol

import csv
import os
from getDictBySubcategory import getDictBySubcategory
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

test = []

test = getDictBySubcategory(data_dictionary) 
finalCsv =  csv_file_creation(test)
