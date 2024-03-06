def calculate_factorial(x):
    if x == 1:
        return 1
    else:
        return x * calculate_factorial(x - 1)
