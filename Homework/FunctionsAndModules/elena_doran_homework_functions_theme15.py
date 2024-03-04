"""
15. Assign True or False to a variable then print it 
"""

x = True
y = False


def get_boolean(var):
    if var == True:
        print("The variable has", var, "value")
    elif var == False:
        print("The variable has", var, "value")
    else:
        print("Invalid boolean value")


get_boolean(x)
get_boolean(y)
get_boolean(True)
get_boolean(False)
get_boolean(10)
