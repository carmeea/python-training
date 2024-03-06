"""
1. Create a function which prints first 10 natural numbers
"""
def print_10_first_natural_numbers():
    for i in range(1, 11):
        print(i)

print_10_first_natural_numbers()

"""
2. Create a function which prints sum of all numbers from 1 to a given number (e.g. print sum of all numbers from 1 to 5)
"""

def sum_to_selected_number(number):
    sum = 0
    for i in range(1, number+1):
        sum += i
    print("Sum of numbers from 1 to", number, "is", sum)

sum_to_selected_number(7)

"""
3. Create a function with 3 arguments and return average only if is greater than 0
"""

def return_average_only_if_natural(x, y, z):
    total = x + y + z
    average = total / 3
    if average > 0:
        return "The average is: " + str(average)
    else:
        return "Ooups, average is less then 0"
    
return_average_only_if_natural(1, -3, 3)

"""
4. Create a function with a default argument value
"""

def number_of_days(days="365"):
    print("There are " + days + " days in a year!")

number_of_days()

"""
5. Create a function which accepts 3 values and return the maximum value
"""

def return_maximum_value(value1, value2, value3):
    return max(value1, value2, value3)

return_maximum_value(-50, -10, 0)

"""
6. Define a function which accepts a number and return if the number is even or odd
"""

def odd_even_checker(number):
    if number % 2 == 0:
        return "The number given is even: " + str(number)
    else:
        return "The number given is odd: " + str(number)
        
odd_even_checker(13)

"""
7. Define a function that accepts 2 values and print its sum, subtraction and multiplication
"""

def multiple_calculations_of_2_values(value1, value2):
    addition = value1 + value2
    substraction = value1 - value2
    multiplication = value1 * value2
    return addition, substraction, multiplication

calculations = multiple_calculations_of_2_values(13, 21)
print("Addition: " + str(calculations[0]), "Substraction: " + str(calculations[1]), "Multiplication: " + str(calculations[2]))

"""
8. Define a function which ask the user for a number and print “Even” if the number is even or “Odd” if the number is odd
"""

def odd_even_checker():
    number = int(input("Enter a number: "))

    if number % 2 == 0:
        return "The number given is even: " + str(number)
    else:
        return "The number given is odd: " + str(number)
        
odd_even_checker()

"""
9. Define a function that checks if a given number is a prime number​
"""

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

number = int(input("Provide a number: "))
if is_prime(number):
    print("Prime")
else:
    print("Not prime")

"""
10. Define a function which prints all the numbers between 1000 and 2000 which are divisible by 7 but are not a multiple of 5
"""

def numbers_div7_multiple5():
    for num in range(1000, 2001):
        if num % 7 == 0 and num % 5 != 0:
            print(num)
        else:
            None

numbers_div7_multiple5()

"""
11. Create a variable with values [‘Siya’, ‘Tiya’, ‘Guru’, ‘Daksh’, ‘Riya’, ‘Guru’] and return “Guru”
"""

def variable_multiple(list, index):
    list = ["Siya", "Tiya", "Guru", "Daksh", "Riya", "Guru"]
    if index < len(list):
        print(list[index])

variable_multiple(list, index=2)


"""
12. Assign an integer to a variable, then print it
"""

def print_assigned_int():
    int = 55
    print(int)

print_assigned_int()

"""
13. Type a couple of words or a short sentence in a variable, then print it
"""

def print_user_input():
    user_input = str(input())
    print(user_input)

print_user_input()

"""
14. Assign a float with 2 decimals to a variable
"""

def floating_numbers():
    float_number = "{:.2f}".format(3.1234123)
    print(float_number)

floating_numbers()


"""
15. Assign True or False to a variable then print it 
"""

def false_variable():
    variable = False
    print(variable)

false_variable()


"""
16. Calculate the length of a string and return that value
"""

def calc_lenght_of_string():
    string = "ajsdnajsnd"
    length = len(string)
    return length

calc_lenght_of_string()

"""
17. Get the largest and the smallest number from a list
"""

def return_smalles_largest():
    numbers = [1,2,3,4,5,6,7]
    smallest = min(numbers)
    largest = max(numbers)
    return smallest, largest

return_smalles_largest()

"""
18. Assign 3 to variable glass_of_water, print "I drank 3 glasses of water today." and after that assign a new value to our variable. Print the result
"""

def print_variable_sentence():
    variable = "3"
    print("I drank " + variable + " glasses of water today.")

print_variable_sentence()

"""
19. Given a tuple, use a range of indexes to print the third, fourth, and fifth item in the tuple​
"""

def range_index_from_tuple(tuple, start_index, end_index):
    ranged_idex = tuple[start_index:end_index+1]
    for item in ranged_idex:
        print(item)
        
tuple = ("one", "two", "three", "four", "five", "six")        
range_index_from_tuple(tuple, 2, 4)

"""
20. Given a dictionary, add a new key/value to the dictionary and print each item
"""

def dictionary_add_and_print(dictionary, key, value):
    dictionary[key] = value
    for key, value in dictionary.items():
        print(key, ":", value)

dictionary = {"engine": "Diesel", "reliable": "yes"}
new_key = "consumption"
new_value = "6 Liters"
dictionary_add_and_print(dictionary, new_key, new_value)