"""
1. Print your current working directory
"""

import os

current_directory = os.getcwd()
print("The current working directory is:", current_directory)


"""
2. Create a directory with a file inside it
"""

import os

directory_path = "/home/cosmin/work/python-training/Homework/FunctionsAndModules"
directory_name = "homework_directory"
file_name = "homework_file.txt"

os.mkdir(os.path.join(directory_path, directory_name))

file_path = os.path.join(directory_path, directory_name, file_name)

with open(file_path, 'w'):
    pass


"""
3. Print factorial and square of a number
"""

import math

n = 5

factorial = math.factorial(n)
square = math.pow(n, 2)

print(f"Factorial of {n} is: {factorial}")
print(f"Square of {n} is: {square}")


"""
4. Return path of a specific file
"""

"""
5. Print random integer between 0 and 5
"""

"""
6. Print current datetime
"""

"""
7. Print current time
"""

"""
8. Converts a number of seconds to a date
"""

"""
9. Print the value of pi
"""

"""
10. Create your own module and import it in another python file
"""
