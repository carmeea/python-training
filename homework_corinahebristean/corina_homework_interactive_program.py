""""Multi-Currency Converter
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

def convert_from_ron(ron):

    currencies = {
        "lev" : 2.55,
        "nok" : 0.43,
        "forint" : 0.013,
        "euro" : 4.98,
        "usd" : 4.57
    }

for currency_name, currency in currencies.items():
    converted = currency / ron
    print(f"{ron} RON is {converted:.2f} {currency}") 

convert_from_ron(100)
