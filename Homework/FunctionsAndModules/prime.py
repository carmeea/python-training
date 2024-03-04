def isPrime(number):
    for x in range(2, number):
        if number % x == 0:
            return False
    return True
