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

def convert_currency(amount_ron):
    exchange_rates = {
        'NOK': 0.43,
        'BGN': 2.55,
        'HUN': 0.013,
        'EUR': 4.98,
        'USD': 4.57
    }

    converted_amounts = {currency: round(amount_ron * rate, 2) for currency, rate in exchange_rates.items()}

    return converted_amounts

# Convert 100 RON to each currency and print the results
amount_ron = 100
converted_results = convert_currency(amount_ron)

for currency, amount in converted_results.items():
    print(f"{amount_ron} RON is {amount:.2f} {currency}")
