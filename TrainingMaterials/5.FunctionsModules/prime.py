def isPrime(numberToCheck):
    # Loop to devide numbertoCheck by all numbers from 2 to numbertoCheck-1
    for x in range(2, numberToCheck):
        # if remaider is zero, return false and exit function
        if numberToCheck % x == 0:
            return False
    return True
