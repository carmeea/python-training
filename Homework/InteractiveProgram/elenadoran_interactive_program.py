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

amount_ron = 100
exchange_rate_lev = 2.55
exchange_rate_nok = 0.43
exchange_rate_forint = 0.013
exchange_rate_euro = 4.98
exchange_rate_usd = 4.57

amount_lev = amount_ron / exchange_rate_lev
print("Convert RON to lev: ", round(amount_lev, 2))

amount_nok = amount_ron / exchange_rate_nok
print("Convert RON to nok: ", round(amount_nok, 2))

amount_forint = amount_ron / exchange_rate_forint
print("Convert RON to forint: ", round(amount_forint, 2))

amount_euro = amount_ron / exchange_rate_euro
print("Convert RON to euro: ", round(amount_euro, 2))

amount_usd = amount_ron / exchange_rate_usd
print("Convert RON to usd: ", round(amount_usd, 2))
