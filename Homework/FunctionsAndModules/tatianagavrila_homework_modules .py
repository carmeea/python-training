import os
import sys
import math as matematica
import random as r
from datetime import datetime, timedelta

"""
1. Print your current working directory
"""
current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")

"""
2. Create a directory with a file inside it
"""
new_directory = "my_directory"
os.makedirs(new_directory, exist_ok=True)
with open(os.path.join(new_directory, "test.txt"), "w") as file:
    file.write("Hello, this is my file!")
    # Print the directory
created_directory = os.path.abspath(new_directory)
print(f"Directory created: {created_directory}")
    
"""
3. Print factorial and square of a number
"""

"""
4. Return path of a specific file
"""

"""
5. Print random integer between 0 and 5
"""
random_integer = r.randint(0, 5)
print(f"Random integer between 0 and 5: {random_integer}")

"""
6. Print current datetime
"""
current_datetime = datetime.now()
print(f"Current datetime: {current_datetime}")

"""
7. Print current time
"""
current_time = datetime.now().time()
print(f"Current time: {current_time}")

"""
8. Converts a number of seconds to a date
"""

"""
9. Print the value of pi
"""
pi_value = matematica.pi
print(f"The value of pi: {pi_value}")

"""
10. Create your own module and import it in another python file
"""
