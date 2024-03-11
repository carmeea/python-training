
# str1 = 'PyThon'
# str2 = 'pYthon'
# print(str1.casefold() == str2.casefold())  # Output: True

# f3 = open("data.csv", "r")
# for line in f3:
#     print(line, end="")
# f3.close()

# print("\nCheck myOutputFileNew.csv")
# inputFile = open("data.csv", "r")
# outputFile = open("myOutputFileNew.csv", "w")
# msg = inputFile.read(10)
# while len(msg)-100000:
#     outputFile.write(msg)
#     msg = inputFile.read(10)
# inputFile.close()
# outputFile.close()

list = []


# def numbers():
#     number = input("After how many subcategories would you like to search ")
#     return int(number)

def enter_subcategory():
    number = int(input("After how many subcategories would you like to search "))
    for i in range(number):
        subcategory = input(f"Enter {i+1} subcategory: ")
        list.append(subcategory.casefold())
    print(list)
    return list

enter_subcategory()