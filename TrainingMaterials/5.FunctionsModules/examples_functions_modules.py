# Examples Functions and Modules
"""
Write a Python function to sum all the numbers in a list.
Sample List: (9, 2, 3, 0, 8)
Expected Output: 22
Implementation:
1. Define a function named 'sum' that takes a list of numbers as input
2. Initialize a variable 'total' to store the sum of numbers, starting at 0
3. Iterate through each element 'x' in the 'numbers' list
4. Add the current element 'x' to the 'total'
5. Print the final sum stored in the 'total' variable
6. Calling the 'sum' function with a tuple of numbers (8, 2, 3, 0, 7)
"""


def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    print(total)


sum((9, 2, 3, 0, 8))


"""
Write a Python function that takes a list and returns a new list with distinct elements from the first list.
Sample List: [1,2,3,3,3,3,4,5]
Unique List: [1, 2, 3, 4, 5]
Implementation:
1. Define a function named 'unique_list' that takes a list 'l' as input and returns a list of unique elements
2. Create an empty list 'x' to store unique elements
3. Iterate through each element 'a' in the input list 'l'
4. Check if the element 'a' is not already present in the list 'x'
5. If 'a' is not in 'x', add it to the list 'x'
6. Return the list 'x' containing unique elements
7. Print the result of calling the 'unique_list' function with a list containing duplicate elements
"""


def unique_list(l):
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return x


#print(unique_list([1, 2, 3, 3, 3, 3, 4, 5]))


"""
Write a Python function to reverse a string.
Sample String: "1234abcd"
Expected Output: "dcba4321"
Implementation:
1. Define a function named 'string_reverse' that takes a string 'string_1' as input
2. Initialize an empty string 'rstr1' to store the reversed string
3. Calculate the length of the input string 'string_1'
4. Execute a while loop until 'index' becomes 0
5. Concatenate the character at index - 1 of 'string_1' to 'rstr1'
6. Decrement the 'index' by 1 for the next iteration
7. Return the reversed string stored in 'rstr1'
8. Print the result of calling the 'string_reverse' function with the input string '1234abcd'
"""


def string_reverse(string_1):
    rstr1 = ""
    index = len(string_1)

    while index > 0:
        rstr1 += string_1[index - 1]
        index = index - 1
    return rstr1


#print(string_reverse("1234abcd"))


"""
Write a Python function to check whether a number falls within a given range.
Sample number: 5
Expected Output: 5 is in the range
Implementation:
1. Define a function named 'test_range' that checks if a number 'n' is within the range 3 to 8 (inclusive)
2. Check if 'n' is within the range from 3 to 8 (inclusive) using the 'in range()' statement
3. If 'n' is within the range, print that 'n' is within the given range
4. If 'n' is outside the range, print that the number is outside the given range
5. Call the 'test_range' function with the argument 5
"""


def test_range(n):
    if n in range(3, 9):
        print("%s is in the range" % str(n))
    else:
        print("The number is outside the given range.")


#test_range(5)


"""
Write a Python function that accepts a string and counts the number of upper and lower case letters.
Sample String: 'The quick Brow Fox'
Expected Output:
No. of Upper case characters: 3
No. of Lower case Characters: 12
Implementation:
1. Define a function named 'string_test' that counts the number of upper and lower case characters in a string 's'
2. Create a dictionary 'd' to store the count of upper and lower case characters
3. Iterate through each character 'c' in the string 's'
4. Check if the character 'c' is in upper case
5. If 'c' is upper case, increment the count of upper case characters in the dictionary
6. Check if the character 'c' is in lower case
7. If 'c' is lower case, increment the count of lower case characters in the dictionary
8. If 'c' is neither upper nor lower case (e.g., punctuation, spaces), do nothing
9. Print the original string 's', the count of upper case characters and the count of lower case characters
10. Call the 'string_test' function with the input string 'The quick Brown Fox'
"""

def string_test(s):
    d = {"UPPER_CASE": 0, "LOWER_CASE": 0}
    for c in s:
        if c.isupper():
            d["UPPER_CASE"] += 1
        elif c.islower():
            d["LOWER_CASE"] += 1
        else:
            pass

    print("Original String: ", s)
    print("No. of Upper case characters: ", d["UPPER_CASE"])
    print("No. of Lower case Characters: ", d["LOWER_CASE"])


#string_test("The quick Brown Fox")


'''
Write a Python program to get the current time.
'''

import datetime
#print(datetime.datetime.now().time())


'''
Write a Python program to subtract five days from the current date.
'''

from datetime import date, timedelta

dt = date.today() - timedelta(5)
#print('Current Date :',date.today())
#print('5 days before Current Date :',dt)


'''
Write a Python program to generate a float between 0 and 1, inclusive and generate a random float within a specific range.
'''

import random 
def random_number():
    print("Generate a float between 0 and 1, inclusive:")
    print(random.uniform(0, 1))
    print("\nGenerate a random float within a range:")
    random_float = random.uniform(1.0, 3.0)
    print(random_float)

#random_number()


'''
Write a Python program to shuffle the elements of a given list.
'''

import random 
def random_shuffle():
    nums = [1, 2, 3, 4, 5]
    print("Original list:")
    print(nums)
    random.shuffle(nums)
    print("Shuffle list:")
    print(nums)
    words = ['red', 'black', 'green', 'blue']
    print("\nOriginal list:")
    print(words)
    random.shuffle(words)
    print("Shuffle list:")
    print(words)

#random_shuffle()


'''
Write a Python program to generate a random color hex, a random alphabetical string, 
random value between two integers (inclusive) and a random multiple of 7 between 0 and 70.
'''
    
import random
import string

def random_values():
    print("Generate a random color hex:")
    print("#{:06x}".format(random.randint(0, 0xFFFFFF)))
    print("\nGenerate a random alphabetical string:")
    max_length = 255
    s = ""
    for i in range(random.randint(1, max_length)):
        s += random.choice(string.ascii_letters)
    print(s)
    print("Generate a random value between two integers, inclusive:")
    print(random.randint(0, 10))
    print(random.randint(-7, 7))
    print(random.randint(1, 1))
    print("Generate a random multiple of 7 between 0 and 70:")
    print(random.randint(0, 10) * 7)

#random_values()
