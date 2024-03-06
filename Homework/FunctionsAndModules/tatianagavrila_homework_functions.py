"""
1. Create a function which prints first 10 natural numbers
"""
def print_first_10_natural_numbers():
    for i in range(1, 11):
        print(i)
        
"""
2. Create a function which prints sum of all numbers from 1 to a given number (e.g. print sum of all numbers from 1 to 5)
"""
def print_sum_up_to_n(n):
    sum = sum(range(1, n + 1))
    print(f"Sum of numbers from 1 to {n}: {sum}")

"""
3. Create a function with 3 arguments and return average only if is greater than 0
"""
def calculate_average(a, b, c):
    average = (a + b + c) / 3
    return average if average > 0 else None

"""
4. Create a function with a default argument value
"""
def say_hi_to(name="User"):
    print(f"Hello, {name}!")

"""
5. Create a function which accepts 3 values and return the maximum value
"""
def find_maximum(a, b, c):
    return max(a, b, c)

"""
6. Define a function which accepts a number and return if the number is even or odd
"""
def check_even_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

"""
7. Define a function that accepts 2 values and print its sum, subtraction and multiplication
"""
def arithmetic_operations(a, b):
    print(f"Sum: {a + b}")
    print(f"Subtraction: {a - b}")
    print(f"Multiplication: {a * b}")

"""
8. Define a function which ask the user for a number and print “Even” if the number is even or “Odd” if the number is odd
"""
def check_even_odd_user_input():
    user_number = int(input("Enter a number: "))
    result = check_even_odd(user_number)
    print(result)


"""
9. Define a function that checks if a given number is a prime number​
"""

"""
10. Define a function which prints all the numbers between 1000 and 2000 which are divisible by 7 but are not a multiple of 5
"""
def print_numbers_divisible_by_7():
    for num in range(1000, 2001):
        if num % 7 == 0 and num % 5 != 0:
            print(num)

"""
11. Create a variable with values [‘Siya’, ‘Tiya’, ‘Guru’, ‘Daksh’, ‘Riya’, ‘Guru’] and return “Guru”
"""

"""
12. Assign an integer to a variable, then print it
"""
integer_variable = 42
print(integer_variable)

"""
13. Type a couple of words or a short sentence in a variable, then print it
"""
sentence_variable = "Hello, World!"
print(sentence_variable)

"""
14. Assign a float with 2 decimals to a variable
"""
float_variable = 3.14
print(float_variable)

"""
15. Assign True or False to a variable then print it 
"""
string_variable = "Hello, team!"
length_of_string = len(string_variable)
print(length_of_string)

"""
16. Calculate the length of a string and return that value
"""

"""
17. Get the largest and the smallest number from a list
"""
numbers_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
largest_number = max(numbers_list)
smallest_number = min(numbers_list)
print(f"Largest number: {largest_number}, Smallest number: {smallest_number}")

"""
18. Assign 3 to variable glass_of_water, print "I drank 3 glasses of water today." and after that assign a new value to our variable. Print the result
"""
glass_of_water = 3
print(f"I drank {glass_of_water} glasses of water today.")
glass_of_water = 5
print(f"Updated value: {glass_of_water}")

"""
19. Given a tuple, use a range of indexes to print the third, fourth, and fifth item in the tuple​
"""

"""
20. Given a dictionary, add a new key/value to the dictionary and print each item
"""