import json

f = open("Homework/InteractiveProgram/rates.json")
j = json.load(f)

print("Our current rates are:")
for i in j["rates"]:
    print(f"1 {i["currency"]} = {i["value"]} RON")

amount = input("What is the RON amount that you wish to exchange?")
valuta = input("What is the currency you wish to exchange to?")

for i in j["rates"]:
    if i["currency"] == valuta:
        conversie = int(amount) / float(i["value"])
        print(f"The amount of {amount} RON will be converted to {conversie:.2f} {valuta}")
else:
    print("We can't exchange to the selected currency.")

f.close()