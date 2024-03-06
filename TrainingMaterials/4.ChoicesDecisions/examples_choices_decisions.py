# Choices Decisions Examples
# Logical conditions in Python

"""
a == b  # equals
a != b  # not equals
a < b  # less than
a <= b  # less than or equal to
a > b  # greater than
a >= b  # greater then or equal to
"""

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

# case

# For loops are used for iterating over a sequence (list, tuple, dictionary,set,or a string)
books = ["LOTR", "The witcher", "The Hobbit"]
for x in books:
    print(x)

# looping through a string
for x in "banana":
    print(x)

# break statement
books = ["LOTR", "The witcher", "The Hobbit"]
for x in books:
    if x == "LOTR":
        break
    print(x)

# continue
books = ["LOTR", "The witcher", "The Hobbit"]
for x in books:
    if x == "LOTR":
        continue
    print(x)

# range() function
for x in range(2, 7, 3):
    print(x)
else:
    print("We are done")  # else in for? :O

# nested loops
books = ["LOTR", "The witcher", "The Hobbit"]
authors = ["Ion Creanga", "Mihai Eminescu", "Moricz Zsigmond"]
for x in books:
    for y in authors:
        print(x, y)

# pass statement

# while loops
i = 1
while i < 6:
    print(i)
    i += 1

# break / continue / else

# try - except

try:
    print(x)
except Exception:
    print("The variable x is not defined")
else:
    print("All was good")
finally:
    print("Go home")

# raise an exception
i = -1

if x < 0:
    raise Exception("Sorry, only positive numbers allowed")
