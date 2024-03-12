

dictionary = {'pufuleti cu sare': ['https://www.mega-image.ro/Dulciuri-si-snacks/Ciocolata/Batoane/Baton-de-ciocolata-cu-crema-de-rom-30g/p/28815', '100gr', 'calorii'], 'baton cu arahide': ['https://www.mega-image.ro/Dulciuri-si-snacks/Napolitane-biscuiti-si-prajituri/Prajituri-si-rulade/Prajitura-cu-lapte-30g/p/64686', '200gr', 'calorii mici']}
def getSubcategory(dictionary):
    subcategoryList = []
    for val in (i[0] for i in dictionary.values()):
        subcategory = val.split('/')[4]
        subcategoryList.append(subcategory)
    return subcategoryList

print(getSubcategory(dictionary))