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


class rates:
    def __init__(self, currency, value):
        self.currency = currency
        self.value = value

c1 = rates("Lev", 2.55)
c2 = rates("NOK", 0.43)
c3 = rates("Forint", 0.013)
c4 = rates("Euro", 4.98)
c5 = rates("USD", 4.57)

choice = input("let me know to which currency you wish to convert, options are: LEV, NOK, Forint, Euro, USD")
while choice in rates.currency:
    amount = input(f"give me an ammount to change form RON to {choice}"
else:
    print("you have to choose again, please pick a currency from the mentioned ones")

        def converter(self):
        print(f"The RON amount given {amount} can be converted to {} {choice}")
        

amount = input("give me an amount for conversion")
