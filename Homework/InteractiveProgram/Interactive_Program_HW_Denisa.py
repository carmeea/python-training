#Multi-Currency Converter
exchange_rates = {'Lev':2.55,'NOK':0.43,'Forint':0.013,'Euro':4.98,'USD':4.57}
amount_in_RON = 100
selected_currency=input("Please select the currency in which you want to convert the RONs (Lev,NOK,Forint,Euro,USD): ")
amount_converted = amount_in_RON / exchange_rates[selected_currency]
print ("Converted amount is: ",round(amount_converted,2))

amount_Lev = amount_in_RON / exchange_rates['Lev']
amount_NOK = amount_in_RON / exchange_rates['NOK']
amount_Forint= amount_in_RON / exchange_rates['Forint']
amount_Euro = amount_in_RON / exchange_rates['Euro']
amount_USD = amount_in_RON / exchange_rates['USD']
converted_dict = {'Lev':round(amount_Lev,2), 'NOK':round(amount_NOK,2), 'Forint':round(amount_Forint,2),
                      'Euro':round(amount_Euro,2), 'USD':round(amount_USD,2)}
print ("\nThe amount of 100 RON converted in each currency:\n",converted_dict)