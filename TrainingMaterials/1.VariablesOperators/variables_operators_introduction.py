# VARIABLES NAMING CONVENTIONS & ASSIGNEMENT
# Print the Words "Hello World"
print("Hello World")

"""
REFERENCE https://www.w3schools.com/python/python_variables.asp
Variables are names given to data that we need to store.
Your program will allocate storage space on your computer for this data.
When you declare a new variable, you need to give it an initial value
"""
userAge = 0
print(userAge)
userAge, userName = 30, "Peter"
print(userAge, userName)

"""
Variables in Python can only contain letters(a-z,A-Z), numbers, undercodes(_)
Fist character cannot be a number. Are case sensitive
Examples: userName, user_name, userName2
Never 2userName or reserved python words (print,input,while, if)
username <> userName
Conventions: camel case or using uderscore thisIsAVariableName, this_is_a_variable_name
"""

# Assigment Sign
x = 5
y = 10
x = y
print("x=", x)
print("y=", y)

# BASIC OPERATORS

x = 5
y = 2
# Addition
# sum is a rezerved word
suma = x + y
print(suma)

# Substraction
rest = x - y
print(rest)

# Multiplication
mult = x * y
print(mult)

# Division
div = x / y
print(div)

# Floor Division
# rounds down the answers to the nearest whole number
fdiv = x // y
print(fdiv)

# Modulus
# gives the remainder when 5 is devided by 2
mod = x % y
print(mod)

# Exponent
# 5 to the power of 2
exp = x**y
print(exp)

# OTHER ASSIGNMENT OPERATORS
"""Besides = sign, there are other operator like +=, -=, *=, etc
x = x + 2 equivalent to x += 2
REFERENCE https://www.w3schools.com/python/python_operators.asp
"""
x += 2
print(x)
y -= 1
print(y)
x = 5
x *= 3
print(x)
