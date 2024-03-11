dictionary = {
    "pufuleti cu sare": [
        "https://www.mega-image.ro/Dulciuri-si-snacks/Chipsuri/Sare/Snack-Original-165g/p/75363",
        "ingredients",
        "calories",
    ],
    "Biscuiti cu spuma de lapte si cocos 16g": [
        "https://www.mega-image.ro/Dulciuri-si-snacks/Napolitane-biscuiti-si-prajituri/Croissant/Croissant-cu-umplutura-cu-cacao-85g/p/43599",
        "ingredient",
        "calorie",
    ],
}


def getSubcategory(dict):
    subcategoryList = []
    for val in (i[0] for i in dict.values()):
        subcategory = val.split("/")[4]
        subcategoryList.append(subcategory)
    return subcategoryList


print(getSubcategory(dictionary))
