conversion_dict = {
    "Lev" : 2.55,
    "NOK" : 0.43,
    "Forint" : 0.013,
    "Euro" : 4.98,
    "USD" : 4.57
}
amount_ron = 100
print(round(amount_ron / conversion_dict["Lev"],2))
print(round(amount_ron / conversion_dict["NOK"],2))
print(round(amount_ron / conversion_dict["Forint"],2))
print(round(amount_ron / conversion_dict["Euro"],2))
print(round(amount_ron / conversion_dict["USD"],2))
