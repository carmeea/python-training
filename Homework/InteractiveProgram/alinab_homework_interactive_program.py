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

exchange_rate = {"Lev": 2.55, "NOK": 0.43, "Forint": 0.013, "Euro": 4.98, "USD": 4.57}
amount_ron = float(input("Amount in RON: "))
conversion = 0 
for key, value in exchange_rate.items():
    conv = ('%.2f' % (amount_ron / value))
    exchange_rate[key] = conv
print(exchange_rate)
