"""
In this method we will import the csv library and open the file in reading mode, 
then we will use the DictReader() function to read the data of the CSV file. 
This function is like a regular reader, but it maps the information to a dictionary 
whose keys are given by the column names and all the values as keys. 
We will create empty lists so that we can store the values in it. 
Finally, we access the key values and append them into the empty lists and print that list.
"""
# importing the module
import csv

# open the file in read mode
filename = open('myOutputFile.csv', 'r')

# creating dictreader object
file = csv.DictReader(filename)

# creating empty lists
key = []
link = []

# iterating over each row and append
# values to empty list
for col in file:
    key.append(col["_key"])
    link.append(col["link"])

# printing lists
print("KEY: ", key)
print("LINK: ", link)

#file.close()

# row_number = 2
# col_number = 1
# value = list_of_rows[row_number - 1][col_number - 1]
# print('Value in a cell at 2nd row and 1st column : ', value)