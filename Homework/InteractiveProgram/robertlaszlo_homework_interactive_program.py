#tema
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
print("RON amount to the be exchanged: ", amount_ron)
exchange_rate_eur = 4.98
exchange_rate_lev = 2.55
exchange_rate_nok = 0.43
exchange_rate_forint = 0.013
exchange_rate_usd = 4.57
amount_eur = (
    float(amount_ron) / exchange_rate_eur
)
amount_lev = (
    float(amount_ron) / exchange_rate_lev
)
amount_nok = (
    float(amount_ron) / exchange_rate_nok
)
amount_forint = (
    float(amount_ron) / exchange_rate_forint
)
amount_usd = (
    float(amount_ron) / exchange_rate_usd
)
print("Exchanged amount in Euro: ", "{:.2f}".format(amount_eur))
print("Exchanged amount in Leva: ", "{:.2f}".format(amount_lev))
print("Exchanged amount in Norvegian Korona: ", "{:.2f}".format(amount_nok))
print("Exchanged amount in Forint: ", "{:.2f}".format(amount_forint))
print("Exchanged amount in USD: ", "{:.2f}".format(amount_usd))