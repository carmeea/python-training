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
        "https://www.mega-image.ro/Dulciuri-si-snacks/C/Croissant-cu-crema-de-cacao-65g/p/5346",
        "1000gr",
        "199kcal",
    ],
    "Croissanta cu crema de cacao 65g": [
        "https://www.mega-image.ro/Dulciuri-si-snacks/C/Croissant-cu-crema-ddde-cacao-65g/p/5346",
        "1000gr",
        "1300kcal",
    ],
}


def getDictBySubcategory(dictionary):
    new_dict = {}
    for key, val in dictionary.items():
        subcategory = val[0].split("/")[4].lower()
        if result == subcategory:
            new_dict.update({key: val})
    if len(new_dict) < 1:
        raise ValueError("This subcategory does not exist. Try again!")
    return new_dict


print(getDictBySubcategory(dictionary))
