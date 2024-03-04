import os

current_directory = os.getcwd()
print("Current working directory:", current_directory)


def factorial(n):
    result1 = 1
    for i in range(1, n+1):
        result1 *= i
    print("Factorial din", n, "este", result1)

def square(n):
    result2 = n * n
    print("Patratul lui", n, "este", result2)

numar = 5
factorial(numar)
square(numar)


import random

numar_aleator = random.randint(0, 5)
print("Un numar aleator intre 0 si 5 este:", numar_aleator)
