"""
Multi-Currency Converter
Write a function that converts an amount from RON to NOK (Norwegian Kroner), to BGN (Bulgarian Lev),
to HUN (Hungarian Forint), to EUR (Euro), and to USD (Us Dollars).
Use exchange rates:
    1 Lev = 2.55 RON
    1 NOK = 0.43 RON
    1 Forint = 0.013 RON
    1 Euro = 4,98 RON
    1 USD = 4,57 RON
Convert 100 RON to both each currency and print the results, rounded to two decimal places.
"""

currency = {"Lev": 2.55, "NOK": 0.43, "Forint": 0.013, "Euro": 4.98, "USD": 4.57}
print("100 de RON convertiti in:")
for i in currency:
    print(f"{i} = {100 / currency[i]:.2f}")


# class rates:
#     def __init__(self, currency, value):
#         self.currency = currency
#         self.value = value

#     def converter(self, amount):
#         convertedAmount = amount / self.value
#         return convertedAmount

# c1 = rates("Lev", 2.55)
# c2 = rates("NOK", 0.43)
# c3 = rates("Forint", 0.013)
# c4 = rates("Euro", 4.98)
# c5 = rates("USD", 4.57)

# choice = input("let me know to which currency you wish to convert, options are: LEV, NOK, Forint, Euro, USD")
# valid = [c.currency.upper() for c in [c1, c2, c3, c4, c5]]

# while choice not in valid:
#     print("you have to choose again, please pick a currency from the mentioned ones")

# amount = input(f"give me an ammount to change form RON to {choice}"


# amount = input("give me an amount for conversion")
