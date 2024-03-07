"""
1. Create a function which prints first 10 natural numbers
"""


def natural_numbers():
    for i in range(1, 11):
        print(i)


natural_numbers()

"""
2. Create a function which prints sum of all numbers from 1 to a given number (e.g. print sum of all numbers from 1 to 5)
"""


def sum_of_numbers():

    n = int(input("Enter a number: "))
    sum = 0
    for i in range(1, n + 1):
        sum += i

    print("Sum = ", sum)


sum_of_numbers()

"""
3. Create a function with 3 arguments and return average only if is greater than 0
"""


def average_calc(arg1, arg2, arg3):
    average = (arg1 + arg2 + arg3) / 3

    if average > 0:
        return average
    else:
        print("It's not greater than 0")


result = average_calc(10, 2, 1)
print(result)


"""
4. Create a function with a default argument value
"""

"""
5. Create a function which accepts 3 values and return the maximum value
"""


def maximum_value(a, b, c):
    return max(a, b, c)


max_value = maximum_value(99, 15, 20)
print("Maximum value:", max_value)

"""
6. Define a function which accepts a number and return if the number is even or odd
"""


# def odd_or_even_number(number):

#     if number % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"


# number = int(input("Enter a number:"))
# result = odd_or_even_number(number)
# print(f"The number {number} is {result}")


"""
7. Define a function that accepts 2 values and print its sum, subtraction and multiplication
"""


def operations(value1, value2):

    sum_result = value1 + value2
    subtraction_result = value1 - value2
    multiplication_result = value1 * value2

    print("Sum:", sum_result)
    print("Subtraction:", subtraction_result)
    print("Multiplication:", multiplication_result)


operations(20, 2)

"""
8. Define a function which ask the user for a number and print “Even” if the number is even or “Odd” if the number is odd
"""


def even_or_odd():
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")


even_or_odd()

"""
9. Define a function that checks if a given number is a prime number​
"""

"""
10. Define a function which prints all the numbers between 1000 and 2000 which are divisible by 7 but are not a multiple of 5
"""

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
