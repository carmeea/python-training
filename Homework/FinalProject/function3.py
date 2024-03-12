#from functia_1_process_user_input import process_user_input
userInput = 'Ciocolata'
dictionary = {'pufuleti cu sare': ['https://www.mega-image.ro/Dulciuri-si-snacks/Ciocolata/Batoane/Baton-de-ciocolata-cu-crema-de-rom-30g/p/28815', '100gr', 'calorii'], 'baton cu arahide': ['https://www.mega-image.ro/Dulciuri-si-snacks/Napolitane-biscuiti-si-prajituri/Prajituri-si-rulade/Prajitura-cu-lapte-30g/p/64686', '200gr', 'calorii mici']}
def getSubcategory(dictionary):
    subcategoryList = []
    new_dict = {}
    for val in (i[0] for i in dictionary.values()):
        subcategory = val.split('/')[4]
        subcategoryList.append(subcategory)
        if userInput != subcategory:
            print(subcategory, userInput)
            for key in dictionary.keys():
                print(key)
                new_dict.setdefault(key,[]).append(dictionary[key])
    return new_dict
#    return subcategoryList



print(getSubcategory(dictionary))