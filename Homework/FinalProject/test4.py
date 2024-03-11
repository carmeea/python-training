# importing the module
import csv

result = {}

with open('myOutputFile.csv', 'r') as file: # pass the file object to DictReader() to get the DictReader object
    dict_reader = csv.DictReader(file) # get a list of dictionaries from dct_reader
    #list_of_dict = list(dict_reader) # print list of dict i.e. rows
    # data = [row for row in dict_reader]
    # print(data)
#     for row in dict_reader:
#         result[row['_key']] = row['_key']
#         result[row['link']] = row['link']
# print(result)
    #next(file)
    myTuples = []
    for row in dict_reader:
        myTuples.append(tuple([row['_key'], row['link']]))

    result = dict(myTuples)
print(result)

    #print(list_of_dict)
        
    # key.append(col["_key"])
    # link.append(col["link"])