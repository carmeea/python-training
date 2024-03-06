
#1. Create a function which prints first 10 natural numbers
#%%
def natural_numbers():
    for i in range(1, 11):
        print(i)
natural_numbers()

# 2. Function to print sum of all numbers from 1 to a given number
#%%
def sum(n):
    total = 0
    for i in range(1, n+1):
        total += i
    print("Sum of numbers from 1 to", n, "is:", total)
n = int(input("Enter a valid number:"))  
sum(n)   
#%%
# 3. Function to return average of three numbers if greater than 0
def average(a, b, c):
    total = a + b + c
    avg = total / 3
    if avg > 0:
        return avg
a = int(input("Enter a valid number: "))  
b = int(input("Enter a valid number: "))  
c = int(input("Enter a valid number: "))  
print(int(average(a, b, c)))
#%%
# 4. Function with a default argument value
def sum(n=10):
    total = 0
    for i in range(1, n+1):
        total += i
    print("Sum of numbers from 1 to", n, "is:", total) 
sum()   
#%%
# 5. Function to return maximum value among three values

def maximum_value(a, b, c):
    return max(a, b, c)
a = int(input("Enter a valid number: "))  
b = int(input("Enter a valid number: "))  
c = int(input("Enter a valid number: ")) 
print(maximum_value(a, b, c))

#%%

# 6. Function to check if a number is even or odd
def even_or_odd(number):
    if number % 2 == 0:
        return True
    else:
        return False
print(even_or_odd(2))


# 7. Function to print sum, subtraction, and multiplication of two values
#%%
def operations(a, b):
    print("Sum:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)

a = int(input("a = "))
b = int(input("b = "))
operations(a, b)
#%%
# 8. Function to determine if a number is even or odd based on user input
number = int(input("Enter a number: "))
if even_or_odd(number) == False:
    print("The number is Odd")
else:
     print("The number is Even")   

#%%
# 9. Function to check if a given number is prime
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

print(is_prime(13))
#%%
# 10. Function to print numbers between 1000 and 2000 divisible by 7 but not multiple of 5
def divisible_by_7_not_multiple_of_5():
    for num in range(1000, 2001):
        if num % 7 == 0 and num % 5 != 0:
            print(num)


# %%
