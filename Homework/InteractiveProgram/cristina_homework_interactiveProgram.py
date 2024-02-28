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


def converter(ron):
    nok = 1 / 0.43 * ron
    bgn = 1 / 2.55 * ron
    hun = 1 / 0.013 * ron
    eu = 1 / 4.98 * ron
    us = 1 / 4.57 * ron

    print(round(nok, 2))
    print(round(bgn, 2))
    print(round(hun, 2))
    print(round(eu, 2))
    print(round(us, 2))


converter(100)
