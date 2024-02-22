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

exchangeLev = 2.55
exchangeNok = 0.43
exchangeForint = 0.013
exchangeEuro = 4.98
exchangeUsd = 4.57

totalRonToExchange = 100

print(f"{totalRonToExchange} RON exchanged into LEV: \n")
totalLEV = totalRonToExchange / exchangeLev
print (round(totalLEV,2))

print(f"{totalRonToExchange} RON exchanged into NOK: \n")
totalNOK = totalRonToExchange / exchangeNok
print (round(totalNOK,2))

print(f"{totalRonToExchange} RON exchanged into Forint: \n")
totalForint = totalRonToExchange/exchangeForint
print (round(totalForint,2))

print(f"{totalRonToExchange} RON exchanged into EUR: \n")
totalEUR = totalRonToExchange/exchangeEuro
print (round(totalEUR,2))

print(f"{totalRonToExchange} RON exchanged into USD: \n")
totalUSD = totalRonToExchange/exchangeUsd
print (round(totalUSD,2))