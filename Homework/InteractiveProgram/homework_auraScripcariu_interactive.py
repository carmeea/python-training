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


# amount_ron = input("Insert the amount in RON: ")
amount_ron = 100
print("RON amount to the be exchanged: ", amount_ron)

exchange_rates = {"exchange_rate_nok": 0.43, "exchange_rate_bgn": 2.55, "exchange_rate_hun": 0.013, "exchange_rate_eur": 4.98, "exchange_rate_usd": 4.57}

amount_nok = (
    int(amount_ron) / float(exchange_rates["exchange_rate_nok"])
)
print("Amount in Norvegian Kroner is:", round(amount_nok, 2))

amount_bgn = (
    int(amount_ron) / float(exchange_rates["exchange_rate_bgn"])
)
print("Amount in Bulgarian Lev is:", round(amount_bgn, 2))

amount_hun = (
    int(amount_ron) / float(exchange_rates["exchange_rate_hun"])
)
print("Amount in Hungarian Forint is:", round(amount_hun, 2))

amount_eur = (
    int(amount_ron) / float(exchange_rates["exchange_rate_eur"])
)
print("Amount in Euro is:", round(amount_eur, 2))

amount_usd = (
    int(amount_ron) / float(exchange_rates["exchange_rate_usd"])
    )
print("Amount in US dolars is:", round(amount_usd, 2))