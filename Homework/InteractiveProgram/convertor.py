import json

f = open("Homework/InteractiveProgram/rates.json")
j = json.load(f)

print("our current rates are:")
for i in j["value"]:
    print(i)


# amount = input("what is the RON amount that you wish to exchange")
# valuta = input("what is the currency you wish to exchange to")

# for valuta in j["currency"]:
#     print(f"The amount of {amount} RON will be converted to {amount/int(f["value"])}.2f {valuta}")

f.close()