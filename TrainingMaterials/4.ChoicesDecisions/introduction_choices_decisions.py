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
