"""
14. Assign a float with 2 decimals to a variable
"""

number = 3.141592


def print_variable(num):
    print("The number is", num)
    print(f"The number is {num:.2f}")
    message1 = "The number is %.2f" % (num)
    print(message1)
    message2 = "The number is {0:.2f}".format(num)
    print(message2)


print_variable(number)
print_variable(100.12345)
