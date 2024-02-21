# Multi-Currency Converter
# Write a function that converts an amount from RON to NOK (Norwegian Kroner), to BGN (Bulgarian Lev),
# to HUN (Hungarian Forint), to EUR (Euro), and to USD (Us Dollars).
# Use exchange rates:
#   1 Lev = 2.55 RON
#   1 NOK = 0.43 RON
#   1 Forint = 0.013 RON
#   1 Euro = 4,98 RON
#   1 USD = 4,57 RON
# Convert 100 RON to both each currency and print the results, rounded to two decimal places.

exchange_rates = {"NOK": 0.43, "BGN": 2.55, "HUN": 0.013, "EUR": 4.98, "USD": 4.57}


def multi_currency_converter(amount, currency):
    if currency == "NOK":
        return amount / exchange_rates["NOK"]
    elif currency == "BGN":
        return amount / exchange_rates["BGN"]
    elif currency == "HUN":
        return amount / exchange_rates["HUN"]
    elif currency == "EUR":
        return amount / exchange_rates["EUR"]
    else:
        return amount / exchange_rates["USD"]

amount = 100
for i in exchange_rates.keys():
    print(round(multi_currency_converter(amount, i),2))

