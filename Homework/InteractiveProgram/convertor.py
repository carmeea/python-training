import json

f = open("Homework/InteractiveProgram/rates.json")
j = json.load(f)

<<<<<<< HEAD
<<<<<<< HEAD
print("Our current rates are:")
for i in j["rates"]:
    print(f"1 {i['currency']} = {i['value']} RON")

amount = input("What is the RON amount that you wish to exchange?\n")

while not(amount.isnumeric() and int(amount) > 0):
    print("The amount specified is not valid!")
    amount = input("Give us another amount that you would like to exchange\n")
else:    
    valuta = input("What is the currency you wish to exchange to?\n")
    found = False

    for i in j["rates"]:
        if i["currency"] == valuta:
            conversie = int(amount) / float(i["value"])
            print(f"The amount of {amount} RON will be converted to {conversie:.2f} {valuta}")
            found = True
            break

    if not found:
        print("We can't exchange to the selected currency. Good day!")
=======
print("our current rates are:")
for i in j["value"]:
=======
print("Our current rates are:")
for i in j["rates"]:
    print(f"1 {i['currency']} = {i['value']} RON")

amount = input("What is the RON amount that you wish to exchange?\n")

while int(amount) <= 0:
    print("The amount specified is not valid!")
    amount = input("Give us another amount that you would like to exchange\n")
else:    
    valuta = input("What is the currency you wish to exchange to?\n")
    found = False

    for i in j["rates"]:
        if i["currency"] == valuta:
            conversie = int(amount) / float(i["value"])
            print(f"The amount of {amount} RON will be converted to {conversie:.2f} {valuta}")
            found = True
            break

    if not found:
        print("We can't exchange to the selected currency.")

f.close()