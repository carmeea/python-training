"""
1. Create a function which prints first 10 natural numbers
"""
def natural_numbers():
    for i in range(10):
        print(i+1)

natural_numbers()

"""
2. Create a function which prints sum of all numbers from 1 to a given number (e.g. print sum of all numbers from 1 to 5)
"""

def factorial_sum(number):
    sum = 0
    for i in range(int(number)):
        sum = sum + i
    print(sum)

factorial_sum(5)

"""
3. Create a function with 3 arguments and return average only if is greater than 0
"""

def average(nr1, nr2, nr3):
    sum = nr1 + nr2 + nr3
    avg = sum / 3
    if avg > 0:
        return avg
    else:
        print("average is less than 0")

average(1,-9,3)

"""
4. Create a function with a default argument value
"""
def name(name = "No name given"):
    return name

name(input("Insert your name: "))

"""
5. Create a function which accepts 3 values and return the maximum value
"""

def max_number(nr1,nr2,nr3):
    max = 0
    if nr1 >= nr2 and nr1 >= nr3: 
        max = nr1
    elif nr2 >= nr1 and nr2 >= nr3:
        max = nr2
    elif nr3 >= nr1 and nr3 >= nr2:
        max = nr3
    return max

max_number(3,3,3)

"""
6. Define a function which accepts a number and return if the number is even or odd
"""

def even_or_odd(number):
    if number % 2 ==0:
        print("even") 
    else:
        print("odd") 

even_or_odd(13)
    
"""
7. Define a function that accepts 2 values and print its sum, subtraction and multiplication
"""

def calculator(nr1, nr2):
    return "sum = " + str( nr1 + nr2), "sub = " + str(nr1 - nr2), "mult = " + str( nr1 * nr2)

calculator(int(input('insert 1st number: ')), int(input('insert 2nd number: ')))

"""
8. Define a function which ask the user for a number and print “Even” if the number is even or “Odd” if the number is odd
"""

def even_or_odd_2(number):
    if number % 2 == 0:
        print('even')
    else:
        print('odd')
    
even_or_odd_2(int(input('insert a number: ')))

"""
9. Define a function that checks if a given number is a prime number​
"""

def is_prime(number):
    flag = 0
    for i in range(2, number):
        if number % i != 0:
            continue
        else:
            flag = 1

    if flag == 0:
        print(str(number) + ' is prime')
    else:
        print(str(number) + ' is not prime')

is_prime(13)

"""
10. Define a function which prints all the numbers between 1000 and 2000 which are divisible by 7 but are not a multiple of 5
"""

def numbers_that_validate_conditions():
    validated_numbers = []
    for i in range(2001):
        if i >= 1000 and i % 7 == 0 and not i % 5 == 0:
            validated_numbers.append(i)
    print(validated_numbers)

numbers_that_validate_conditions()

"""
11. Create a variable with values [‘Siya’, ‘Tiya’, ‘Guru’, ‘Daksh’, ‘Riya’, ‘Guru’] and return “Guru”
"""

"""
12. Assign an integer to a variable, then print it
"""

x = 5 
print(x)

"""
13. Type a couple of words or a short sentence in a variable, then print it
"""

essay = "this is a beautiful essay"
print(essay)

"""
14. Assign a float with 2 decimals to a variable
"""

var = 1.22
print(var)

"""
15. Assign True or False to a variable then print it 
"""

var = True
print (var)

"""
16. Calculate the length of a string and return that value
"""

print(len(input('Please insert something: ')))

"""
17. Get the largest and the smallest number from a list
"""

interesting_list = [1, 5, 2, 22, -50]

print(min(interesting_list), max(interesting_list))

"""
18. Assign 3 to variable glass_of_water, print "I drank 3 glasses of water today." and after that assign a new value to our variable. Print the result
"""

glass_of_water = 3
print(f"I drank {glass_of_water} glasses of water today.")

glass_of_water = 5
print(f"I drank {glass_of_water} glasses of water today.")

"""
19. Given a tuple, use a range of indexes to print the third, fourth, and fifth item in the tuple​
"""

my_tuple = (1,2,"water", "game", "python", 3.14, ['new', 'season'])

for i in range(len(my_tuple)):
    if i in (2,3,4):
        print(my_tuple[i])
    
"""
20. Given a dictionary, add a new key/value to the dictionary and print each item
"""
my_dict = {"name": "razvan",
           "job": "automation tester",
           "programming_language": "python"}
print(my_dict)
my_dict["hobbies"] = ["gaming", "anime"]
print(my_dict)