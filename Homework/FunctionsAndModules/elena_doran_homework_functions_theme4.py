"""
4. Create a function with a default argument value
"""


def calculate_operations(x=8, y=3):
    print("Addition is :", x + y)
    print("Substraction is :", x - y)
    print("Multiplication is :", x * y)
    print("Division is :", x / y)
    print("Floor Division is :", x // y)
    print("Modulus is :", x % y)
    print("Exponent is :", x**y)


calculate_operations()
calculate_operations(3, 4)
