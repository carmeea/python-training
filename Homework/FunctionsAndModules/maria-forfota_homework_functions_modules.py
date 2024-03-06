"""
1. Create a function which prints first 10 natural numbers
"""


def printFirstTenNumbers():
    for num in range(1, 11):
        print(num)


printFirstTenNumbers()

"""
2. Create a function which prints sum of all numbers from 1 to a given number (e.g. print sum of all numbers from 1 to 5)
"""


def printTheSum(givenNumber):
    sum = 0
    for num in range(1, givenNumber + 1):
        sum += num
    print(sum)


printTheSum(6)

"""
3. Create a function with 3 arguments and return average only if is greater than 0
"""


def averageGreaterThanZero(arg1, arg2, arg3):
    average = (arg1 + arg2 + arg3) / 3
    if average > 0:
        print(average)


averageGreaterThanZero(1, 2, 3)

"""
4. Create a function with a default argument value
"""


def defaultArgumentFunction(name="Maria"):
    print("Hello, " + name + "!")


defaultArgumentFunction()


"""
5. Create a function which accepts 3 values and return the maximum value
"""


def findMaximum(val1, val2, val3):
    print(max(val1, val2, val3))


findMaximum(10, 2, 6)
"""
6. Define a function which accepts a number and return if the number is even or odd
"""


def isEvenOrOdd(num):
    if num % 2 == 0:
        print(f"The number: {num} is even ")
    else:
        print(f"The number: {num} is odd ")


isEvenOrOdd(4)

"""
7. Define a function that accepts 2 values and print its sum, subtraction and multiplication
"""


def performOperations(num1, num2):
    sum = num1 + num2
    print(f"The sum  is {sum}")
    multiplication = num1 * num2
    print(f"The multiplication is {multiplication}")
    substraction = num1 - num2
    print(f"The substraction is {substraction}")


performOperations(4, 3)
"""
8. Define a function which ask the user for a number and print “Even” if the number is even or “Odd” if the number is odd
"""


def askUserForNumber():
    number = int(input("Please enter a number: "))
    isEvenOrOdd(number)


"""
askUserForNumber()
"""
"""
9. Define a function that checks if a given number is a prime number​
"""


def checkIfPrime(number):
    for num in range(2, number):
        if number % num == 0:
            return False
        return True


checkIfPrime(13)

"""
10. Define a function which prints all the numbers between 1000 and 2000 which are divisible by 7 but are not a multiple of 5
"""


def printNumbers():
    for num in range(1000, 2001):
        if num % 7 == 0 and num % 5 != 0:
            print(num)


printNumbers()
"""
11. Create a variable with values [‘Siya’, ‘Tiya’, ‘Guru’, ‘Daksh’, ‘Riya’, ‘Guru’] and return “Guru”
"""

"""
12. Assign an integer to a variable, then print it
"""

"""
13. Type a couple of words or a short sentence in a variable, then print it
"""

"""
14. Assign a float with 2 decimals to a variable
"""

"""
15. Assign True or False to a variable then print it 
"""

"""
16. Calculate the length of a string and return that value
"""

"""
17. Get the largest and the smallest number from a list
"""

"""
18. Assign 3 to variable glass_of_water, print "I drank 3 glasses of water today." and after that assign a new value to our variable. Print the result
"""

"""
19. Given a tuple, use a range of indexes to print the third, fourth, and fifth item in the tuple​
"""

"""
20. Given a dictionary, add a new key/value to the dictionary and print each item
"""
