"""
1. Create a function which prints first 10 natural numbers
"""

def print_first_ten_natural_num():
    for i in range(1, 11):
        print(i)


print_first_ten_natural_num()


"""
2. Create a function which prints sum of all numbers from 1 to a given number (e.g. print sum of all numbers from 1 to 5)
"""

def sum_of_num(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    print("The sum of all numbers from 1 to", n, "is:", total)

sum_of_num(5)  



"""
3. Create a function with 3 arguments and return average only if is greater than 0
"""

def calculate_average(x, y, z):
    total = x + y + z
    average = total / 3
    if average > 0:
        return average
    else:
        return None


result = calculate_average(2, 4, 6)
if result is not None:
    print("Average:", result)
else:
    print("Average is not greater than 0.")


"""
4. Create a function with a default argument value
"""

def salute (name="World"):
    print("Hello,", name)

salute()  
salute("Dan")  


"""
5. Create a function which accepts 3 values and return the maximum value
"""
def max_num (a, b, c):
    return max(a, b, c)

# Example usage:
print(max_num(5, 9, 3))  
print(max_num(10, 2, 8))  
print(max_num(1, 1, 1))   




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