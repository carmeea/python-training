def multi_currency_converter(ron_amount):
    lev_rate = 2.55
    nok_rate = 0.43
    forint_rate = 0.013
    euro_rate = 4.98
    usd_rate = 4.57

    lev_amount = ron_amount / lev_rate
    nok_amount = ron_amount / nok_rate
    forint_amount = ron_amount / forint_rate
    euro_amount = ron_amount / euro_rate
    usd_amount = ron_amount / usd_rate

    print(f"Amount in RON: {ron_amount}")
    print(f"BGN: {round(lev_amount, 2)}",)
    print(f"NOK: {round(nok_amount, 2)}")
    print(f"HUN: {round(forint_amount, 2)}")
    print(f"EUR: {round(euro_amount, 2)}")
    print(f"USD: {round(usd_amount, 2)}")
    
amount_in_ron = 100
multi_currency_converter(amount_in_ron)