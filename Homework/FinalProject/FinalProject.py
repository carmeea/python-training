"""
Given the data.csv file, find all products for a subcategory.
_key,
link,
nutritional_info/Grasimi,
nutritional_info/Valoare energetica,
nutritional_info/Glucide,
nutritional_info/Fibre,
nutritional_info/Sodiu,
nutritional_info/Proteine,
nutritional_info/Grasimi saturate,
Ingrediente,
Alergeni

Function1: read file
Function2: Find all products for a subcategory given by the user 
            Subcategory search should not be case sesitive
Function3: export them (write) to another CSV file. 
Function4: If subcategory is not found throw an error back to the user and do not create the file.
Function5: If products are found, notify user that file was created succesfully, specify also the file name.

1.Find all products for a subcategory given by the user and export them (write) 
to another CSV file. 


2.Subcategory will be given as input from user.
ex: Category=Dulciuri si Snacks, Subcategoy=Napolitane biscuiti si prajituri, Ciocolata, Chipsuri
Subcategory search should not be case sesitive. For example user can give as input 
->NaPOLItane Biscuiti SI prajiturI
-> check in link: https://www.mega-image.ro/Dulciuri-si-snacks .....   that the value exists
-> ex: search after "pufuleti" -> should return all values for _key

3.If subcategory is not found throw an error back to the user and do not create the file.
-> we can create a list and search after each item for the list
    -> search after existing category(a) and non-existing category(b) 
        -> create file for (a) and not file created (b)
 
4.If products are found, notify user that file was created succesfully, specify also the file name.

Note: Apply concepts from previous lessons (data types,  loops, exception handling, files management, 
functions, etc)
"""
