from functia_1_process_user_input import result

dictionary = {
    "pufuleti cu sare": [
        "https://www.mega-image.ro/Dulciuri-si-snacks/Ciocolata/Batoane/Baton-de-ciocolata-cu-crema-de-rom-30g/p/28815",
        "100gr",
        "calorii",
    ],
    "baton cu arahide": [
        "https://www.mega-image.ro/Dulciuri-si-snacks/Napolitane-biscuiti/Prajitura-cu-lapte-30g/p/64686",
        "200gr",
        "calorii mici",
    ],
    "Croissant cu crema de cacao 65g": [
        "https://www.mega-image.ro/Dulciuri-si-snacks/Croissant si cola/Croissant-cu-crema-de-cacao-65g/p/5346",
        "1000gr",
        "199kcal",
    ],
}


def getDictBySubcategory(dictionary):
    new_dict = {}
    for key, val in dictionary.items():
        subcategory = "".join(val).split("/")[4].lower()
        if result == subcategory:
            new_dict = {key: val}
    return new_dict


print(getDictBySubcategory(dictionary))
