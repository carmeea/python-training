list = []

def enter_subcategory():
    number = int(input("After how many subcategories would you like to search "))
    for i in range(number):
        subcategory = input(f"Enter {i+1} subcategory: ")
        list.append(subcategory.casefold())
    print(list)
    return list

enter_subcategory()