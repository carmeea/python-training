"""
1. Create a function which prints first 10 natural numbers
"""
def natural_numbers(numbers):
    print("The first 10 natural numbers are:")
    for i in range(numbers):
        print(i)

natural_numbers(10)

"""
2. Create a function which prints sum of all numbers from 1 to a given number (e.g. print sum of all numbers from 1 to 5)
"""
def suma(numarul):
    total = 0
    print("Suma este:")
    for i in range(numarul):
        total += i+1
    print(total)

user_input = input("give me an integer for calculating the sum of all integers starting from 1 to the given number")
suma(int(user_input))

"""
3. Create a function with 3 arguments and return average only if is greater than 0
"""
def average():
    x = input("give me the first number for the average: ")
    y = input("second number for the average: ")
    z = input("3rd number for the average: ")
    media = 0
    media = (int(x)+int(y)+int(z))/3
    print(media) if media >0 else print("average is not greater than 0")

average()



"""
4. Create a function with a default argument value
"""
def average(x=10, y=567, z=999):
    media = 0
    media = (x+y+z)/3
    print(media) if media >0 else print("average is not greater than 0")

average()

"""
5. Create a function which accepts 3 values and return the maximum value
"""
def maximul():
    print("give me 3 numbers for comparison:\n")
    list1=[]
    for i in range(3):
        list1.append(int(input()))
    #print(list1)
    print(max(list1))

maximul()

"""
6. Define a function which accepts a number and return if the number is even or odd
"""
def even_check(x):
    print("it's odd") if int(x) %2 == 0 else print("it's even")

print("give me a number for establishing if it's odd or even:\n")
even_check(input())

"""
7. Define a function that accepts 2 values and print its sum, subtraction and multiplication
"""
def calculation():
    x=int(input("input the first number: "))
    y=int(input("input the second number: "))
    print(f" suma este {x+y}\n diferenta este {x-y}\n inmultirea este {x*y}")

calculation()

"""
8. Define a function which ask the user for a number and print “Even” if the number is even or “Odd” if the number is odd
"""
def even_check(x):
    print("Odd") if int(x) %2 == 0 else print("Even")

print("give me a number for establishing if it's odd or even:\n")
even_check(input())

"""
9. Define a function that checks if a given number is a prime number​
"""
def is_prime(x):
    for i in range(2, int(x)+1):
        if int(x) % i == 0:
                return False
        return True
        
user_input=input("give me a number for the check ")
if is_prime(user_input) and (int(user_input)>1):
     print("is prime")
else:
     print("not prime")

"""
10. Define a function which prints all the numbers between 1000 and 2000 which are divisible by 7 but are not a multiple of 5
"""
def printout():
    results = []
    for i in range(1000, 2000, 5):
        if i % 7 == 0:
            results.append(i)
    print(results)

printout()

"""
11. Create a variable with values [‘Siya’, ‘Tiya’, ‘Guru’, ‘Daksh’, ‘Riya’, ‘Guru’] and return “Guru”
"""
def parse():
    names=["Siya", "Tiya", "Guru", "Daksh", "Riya", "Guru"]
    for i in names:
        if i == "Guru":
            print(i)

parse()

"""
12. Assign an integer to a variable, then print it
"""
def inttovar():
    x = 7
    print(x)

inttovar()

"""
13. Type a couple of words or a short sentence in a variable, then print it
"""
def sentence():
    phrase="Asa e usor a scrie renumitul si utilul numar"
    print(phrase)

sentence()

"""
14. Assign a float with 2 decimals to a variable
"""
def my_function():
    x= 3.14
    print(x)

my_function()

"""
15. Assign True or False to a variable then print it 
"""
def adevara():
    t = True
    print(t)

adevara()

"""
16. Calculate the length of a string and return that value
"""
def lungime(x):
    lungime=0
    for i in x:
        lungime+=1
    print(f"length is: {lungime}")

print("give me a word for me to calculate it's length")
lungime(input())

"""
17. Get the largest and the smallest number from a list
"""
def minmax():
    list=[]
    list_lengt=input("how many numbers do you want to be analyzed? ")
    print("give me the numbers:\n")
    for i in range(int(list_lengt)):
        list.append(input())
    print(f"\nlargest number in list is: {max(list)}")
    print(f"smallest number in list is: {min(list)}")

minmax()

"""
18. Assign 3 to variable glass_of_water, print "I drank 3 glasses of water today." and after that assign a new value to our variable. Print the result
"""

def drinking():
    glass_of_water=3
    sentence = "I drank {} glasses of water today."
    print(sentence.format(glass_of_water))
    glass_of_water=5
    print(sentence.format(glass_of_water))

drinking()

"""
19. Given a tuple, use a range of indexes to print the third, fourth, and fifth item in the tuple​
"""
def month_txt(x,y,z):
    luni = ("Ianuarie", "Februarie", "Martie", "Aprilie", "Mai", "Iunie", "Iulie", "August", "Septembrie", "Octombrie", "Noiembrie", "Decembrie")
    print(f" a {x}-a luna este {luni[x-1]}\n a {y}-a luna este {luni[y-1]}\n a {z}-a luna este {luni[z-1]}")
    
month_txt(3,4,5)

"""
20. Given a dictionary, add a new key/value to the dictionary and print each item
"""
this_dict = { "brand": "Ford", "model": "Mustang", "year": 1964}

def add_color(x):
    this_dict["color"] = x

print(this_dict)
print("give me a color for the car")
add_color(input())
print(this_dict)
