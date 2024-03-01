"""
1. Create a function which prints first 10 natural numbers
"""

num = 10


def my_function():
    for i in range(1, num + 1):
        print(i, end=" ")


my_function()


"""
2. Create a function which prints sum of all numbers from 1 to a given number (e.g. print sum of all numbers from 1 to 5)
"""


def addition(user_num):
    if user_num:
        print(user_num)
        return user_num + addition(user_num - 1)
    else:
        return 0


while True:
    try:
        user_num = int(input("Please insert a number >= 1: "))
        if user_num >= 1:
            print("Sum is: ", addition(user_num))
        else:
            print("Number should be >=1, try again!")
            continue
    except ValueError:
        print("Error: You did not enter a number, try again")
        continue
    else:
        break


"""
3. Create a function with 3 arguments and return average only if is greater than 0
"""


def average3num(x, y, z):
    if ((x + y + z) / 3) > 0:
        print((x + y + z) / 3)
    else:
        print("Average is <= 0")


average3num(0, 0, 0)
average3num(-1, -4, 5)
average3num(1, 9, 13)
average3num(1, 2, 0)

"""
4. Create a function with a default argument value
"""


def my_function(name="Aura"):
    print("My name is: " + name)


my_function()

"""
5. Create a function which accepts 3 values and return the maximum value
"""


def maximum(a, b, c):
    list = [a, b, c]
    return max(list)


print(maximum(10, 11, 12))
print(maximum("a", "b", "c"))
print(maximum(1, 15, -3))

"""
6. Define a function which accepts a number and return if the number is even or odd
"""


def even_or_odd_check(number):
    if (number % 2) == 0:
        print("{0} is Even".format(number))
    else:
        print("{0} is Odd".format(number))


even_or_odd_check(20)
even_or_odd_check(11)
even_or_odd_check(0)
even_or_odd_check(-5)

"""
7. Define a function that accepts 2 values and print its sum, subtraction and multiplication
"""


def super_function(x, y):
    addition = x + y
    print("Result of addition is:", addition)
    substraction = x - y
    print("Result of substraction is:", substraction)
    multiplication = x * y
    print("Result of multiplication is:", multiplication)


super_function(1, 0)
super_function(5, 2)
super_function(-1, -10)


"""
8. Define a function which ask the user for a number and print “Even” if the number is even or “Odd” if the number is odd
"""


def even_or_odd_check(number):
    if (number % 2) == 0:
        print("{0} is Even".format(number))
    else:
        print("{0} is Odd".format(number))


while True:
    try:
        user_num = int(input("Enter a number: "))
        even_or_odd_check(user_num)
    except ValueError:
        print("Error: You did not enter a number, try again")
        continue
    else:
        break


"""
9. Define a function that checks if a given number is a prime number
"""


def check_prime_number(num):
    if num > 1:
        # Iterate from 2 to n / 2
        for i in range(2, int(num / 2) + 1):
            # If num is divisible by any number between 2 and n / 2, it is not prime
            if (num % i) == 0:
                print(num, "Number is not prime")
                break
        else:
            print(num, "Number is prime")
    else:
        print("Please insert a number > 0")


check_prime_number(11)
check_prime_number(-3)
check_prime_number(120)
check_prime_number(0)

"""
10. Define a function which prints all the numbers between 1000 and 2000 which are divisible by 7 but are not a multiple of 5
"""

min = 1000
max = 2000


def numbers_check():
    return [n for n in range(min, max + 1) if n % 7 == 0 and n % 5 != 0]


print(numbers_check())


"""
11. Create a variable with values ["Siya", "Tiya", "Guru", "Daksh", "Riya", "Guru"] and return “Guru”
"""

names = ["Siya", "Tiya", "Guru", "Daksh", "Riya", "Guru"]

all_guru = []
for i in range(0, len(names)):
    if names[i] == "Guru":
        all_guru.append(names[i])

print("Guru list : ", all_guru)


"""
12. Assign an integer to a variable, then print it
"""

num = 100

# print num
print("num =", num)
# print using format
print("num = {0}".format(num))

"""
13. Type a couple of words or a short sentence in a variable, then print it
"""

my_words = "Hellow world 1234! Hellow again!"

# print my_words
print("my_words =", my_words)
print("The " + my_words + " are awesome")

"""
14. Assign a float with 2 decimals to a variable
"""

new_number = 4.99
print(f"The {new_number} is your float!")

"""
15. Assign True or False to a variable then print it 
"""

time_to_go_home = True
print(time_to_go_home)
print(f"Is time to go home - {time_to_go_home}")

"""
16. Calculate the length of a string and return that value
"""

my_string = input("Please insert a string:")


def string_length():
    return len(my_string)


print(string_length())

"""
17. Get the largest and the smallest number from a list
"""

input_string = input("Please enter your numbers separated by space \n")
my_list = input_string.split()
print("Strings list: ", my_list)


def calculate_max():
    return max(my_list)


def calculate_min():
    return min(my_list)


try:
    # convert each item to int type
    for i in range(len(my_list)):
        my_list[i] = int(my_list[i])
    print(calculate_max())
    print(calculate_min())
except ValueError:
    print("Error: Please enter only numbers")


"""
18. Assign 3 to variable glass_of_water, print "I drank 3 glasses of water today." and after that assign a new value to our variable. Print the result
"""

glass_of_water = 3
print(f"I drank {glass_of_water} glasses of water today.")

glass_of_water = 22
print("I drank " + str(glass_of_water) + " glasses of water today.")


"""
19. Given a tuple, use a range of indexes to print the third, fourth, and fifth item in the tuple​
"""

rooms = ("ROOM_1", "ROOM_2", "ROOM_3", "ROOM_4", "ROOM_5", "ROOM_6")

i = 0
while i < len(rooms):
    if i == 2 or i == 3 or i == 4:
        print(rooms[i])
    i = i + 1

"""
20. Given a dictionary, add a new key/value to the dictionary and print each item
"""
my_info = {"name": "Iris", "age": 22, "location": "Cluj"}

# print("Dictionary = \n", my_info)

my_info["department"] = "Sales"

# print("\nUpdated Dictionary = \n", my_info)

for k, v in my_info.items():
    print(k, v)
