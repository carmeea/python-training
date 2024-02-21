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


convert_amount_ron = 100
amount_ron = input("Amount in Ron: ")


lev = 2.55
nok = 0.43
forint = 0.013
euro = 4.98
usd = 4.57

# Print statement using % formatter

amount_lev = float(amount_ron)*lev
amount_nok = float(amount_ron)*nok
amount_forint = float(amount_ron)*forint
amount_euro = float(amount_ron)*euro
amount_usd = float(amount_ron)*usd

print("%s Ron = \n%s lev \n%s nok \n%s forint \n%s euro \n%s usd" %(amount_ron, round(amount_lev,2),round(amount_nok,2), round(amount_forint,2),round(amount_euro,2),round(amount_usd,2)))



