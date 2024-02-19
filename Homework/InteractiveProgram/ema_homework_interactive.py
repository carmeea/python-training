"""Multi-Currency Converter
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

def convert_ron(amount_ron):

  exchange_rates = {
        "LEV" : 2.55,
        "NOK" : 0.43,
        "BGN" : 0.013,  
        "HUN" : 4.98,
        "EUR" : 4.57,
        "USD" : 4.57
    }
  
  for currency, rate in exchange_rates.items():
    converted_amount = amount_ron * rate
    print(f"{amount_ron} RON is equal to {converted_amount:.2f} {currency}")

convert_ron(100)
