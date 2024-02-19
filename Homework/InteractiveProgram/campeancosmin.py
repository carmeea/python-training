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

def convert_ron_to_lev(amount):
    lev = amount / 2.55
    two_decimal_result = "{:.2f}".format(lev)
    return two_decimal_result

print(f"100 RON is {convert_ron_to_lev(100)} LEV at the exchange rate of 2.55")


def convert_ron_to_nok(amount):
    nok = amount / 0.43
    two_decimal_result = "{:.2f}".format(nok)
    return two_decimal_result

print(f"100 RON is {convert_ron_to_nok(100)} NOK at the exchange rate of 0.43")


def convert_ron_to_forint(amount):
    forint = amount / 0.013
    two_decimal_result = "{:.2f}".format(forint)
    return two_decimal_result

print(f"100 RON is {convert_ron_to_forint(100)} Forint at the exchange rate of 0.013")


def convert_ron_to_euro(amount):
    euro = amount / 4.98
    two_decimal_result = "{:.2f}".format(euro)
    return two_decimal_result

print(f"100 RON is {convert_ron_to_euro(100)} Euro at the exchange rate of 4.98")


def convert_ron_to_usd(amount):
    usd = amount / 4.57
    two_decimal_result = "{:.2f}".format(usd)
    return two_decimal_result

print(f"100 RON is {convert_ron_to_usd(100)} USD at the exchange rate of 4.57")