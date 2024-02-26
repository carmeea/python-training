<<<<<<< HEAD
# Logical conditions in Python

a == b  # equals
a != b  # not equals
a < b  # less than
a <= b  # less than or equal to
a > b  # greater than
a >= b  # greater then or equal to

# If statements

a = 12
b = 2
if a > b:  # If statement
    print("a este mai mare decat b")
elif a == b:  # Elif statement
    print("a egal cu b")
else:
    print("b este mai mare decat a")

# Carefull with indentions

# Short hand if and if ... else
a = 12
b = 3
if a > b:
    print("a mai mare decat b")

print("A") if a > b else print("B")  # here we can add another if statement

# To combine conditional statements we can use the following keywords
# and | or | not

# Nested IF statements

# pass statement
=======
# Making CHOICES and DECISIONS

# Condition Statements
"""
Most common condition statement is comparison statement x==y
Return will be True or False.
Other comparison signs != (not equal), < (smaller than), >(greather then), 
<= (smaller than or equals to), >= (greather than or equals to)
Logical operators: and, or, not
"""
print(5 != 2)
print(5 >= 5)
print(5 > 2 or 7 > 10 or 3 == 2)  # True
print(5 > 2 and 7 < 10 and 3 == 2)  # False


# IF Statement
"""
Structure statement (you can add multiple elif statements):
if condition 1 is met:
    do A
elif condition 2 is met:
    do B
elif condition 3 is met:
    do C
else:
    do E
"""
userInput = input("Enter 1 or 2:")
print(userInput)
if userInput == "1":
    print("This is option 1")
    print("Hello everybody")
elif userInput == "2":
    print("Python Rocks!")
else:
    print("Invalid valid number.")


# Inline IF
""" Simpler form of if statement
do something if <condition-is-true> else do something else
"""
num1 = 10
print("do Task_A" if num1 == 10 else "do Task_B")


# FOR Loop
# Executes block of code until condition in for is no longer valid
maximum = (3, 2, 1)
for a in maximum:
    print(a)

animals = ["cats", "dogs", "rabbits", "hamsters"]
for myPets in animals:
    print(myPets)
# Display index of items in list - using enumerate()
for index, myPets in enumerate(animals):
    print(index, myPets)

message = "Hello!"
for i in message:
    print(i)

# Looping through a sequence of numbers - using range()
# When using range() if start steps is not given, numbers generate from 0
for i in range(7):
    print(i)  # 0, 1, 2, 3, ..., 6
for i in range(3, 10):
    print(i)  # 3, 4, 5, ..., 9
for i in range(4, 10, 2):
    print(i)  # 4, 6, 8


# WHILE Loop
"""
Repeatedly executes steps inside loop while condition remains valid
while condition is True:
    do A
"""
counter = 5
while counter > 0:
    print("Counter = ", counter)
    counter = counter - 1  # Last step 0>0? False -> Exit

# BREAK
j = 0
for i in range(5):
    j += 2
    print("i=", i, "j=", j)
    if j == 6:
        break

# CONTINUE
# When using continue, the rest of the loop after the keyword is skipped for that iteration
j = 0
for i in range(5):
    j += 2
    print("\ni=", i, "j=", j)
    if j == 6:
        continue
    print("Hello")

# TRY, EXCEPT
"""
Statement controls how the program proceeds when errors occurs
try:
    do something
except:
    do something else when error occurs
"""
try:
    div1 = 12 / 0
    print(div1)
except:
    print("An error occurred!")

# EXCEPTION HANDLING
"""
Many pre-defined error types in python
Link https://docs.python.org/3/library/exceptions.html
IOError:  io error is an exception specific to input and/or output functions (e.g: open a file - "file not found")
ImportError: raised when an import statement fails to find module definition
IndexError: raised when a sequence index (string, list, tuple) is out of range.
KeyError: raised when dictionary key is not found.
NameError: when a local/global name is not found.
TypeError: raised when an operation or function is appliedto an object inappropriate type.

To display  the default ValuError message write:
except ValueError as e:
    print(e)
"""

try:
    div1 = 12 / 0
    print(div1)
except Exception as e:
    print("An error occurred!", e)

# Specifying the error type
# Try this example with values 12 & 0, 12 & 3, entering a string as value
try:
    userInput1 = int(input("Please enter first number:"))
    userInput2 = int(input("Please enter second number:"))
    div1 = userInput1 / userInput2
    print("Division result: ", div1)
    myFile = open("missing.txt", "r")
except ValueError:
    print("Error: You did not enter a number")
except ZeroDivisionError:
    print("Error: Cannot devide by zero")
except Exception as e:
    print("Unknown error: ", e)
>>>>>>> c50ae51 (Added introduction materials for Condition Statements)
