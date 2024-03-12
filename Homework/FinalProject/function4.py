userInput = "Ciocolata"
dictionary = {
    "pufuleti cu sare": [
        "https://www.mega-image.ro/Dulciuri-si-snacks/Ciocolata/Batoane/Baton-de-ciocolata-cu-crema-de-rom-30g/p/28815",
        "100gr",
        "calorii",
    ],
    "baton cu arahide": [
        "https://www.mega-image.ro/Dulciuri-si-snacks/Napolitane-biscuiti-si-prajituri/Prajituri-si-rulade/Prajitura-cu-lapte-30g/p/64686",
        "200gr",
        "calorii mici",
    ],
}


def getDictBySubcategory(dictionary):
    new_dict = {}
    for key, val in dictionary.items():
        subcategory = "".join(val).split("/")[4]
        if userInput == subcategory:
            new_dict = {key: val}
    return new_dict


print(getDictBySubcategory(dictionary))
