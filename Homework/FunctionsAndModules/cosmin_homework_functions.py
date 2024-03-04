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

def sum_numbers():
    try:
        n = int(input("Input a number: "))
        if n < 1:
            print("Input a positive number!")
            return
        
        total_sum = sum(range(1, n + 1))
        print(f"The sum of all numbers from 1 to {n} is: {total_sum}")

    except ValueError:
        print("Please enter a valid number!")

sum_numbers()


"""
3. Create a function with 3 arguments and return average only if is greater than 0
"""

def positive_average(x, y, z):
    average = (x + y + z) / 3
    if average > 0:
        return average
    else:
        return "Average is not greater than 0!"

result = positive_average(6, 12, 2)
print(result)


"""
4. Create a function with a default argument value
"""

"""
5. Create a function which accepts 3 values and return the maximum value
"""

"""
6. Define a function which accepts a number and return if the number is even or odd
"""

"""
7. Define a function that accepts 2 values and print its sum, subtraction and multiplication
"""

"""
8. Define a function which ask the user for a number and print “Even” if the number is even or “Odd” if the number is odd
"""

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
