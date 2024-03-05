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

def convertor(number):
    print(f"{number} RON is converted to {number/2.55:.2f} Lev\n"
          f"{number} RON is converted to {number/0.43:.2f} NOK\n"
          f"{number} RON is converted to {number/0.013:.2f} Forint\n"
          f"{number} RON is converted to {number/4.98:.2f} Euro\n"
          f"{number} RON is converted to {number/4.57:.2f} USD\n")

convertor(100)