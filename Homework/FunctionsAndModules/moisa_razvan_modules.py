"""
1. Print your current working directory
"""
import os
print(os.getcwd())

"""
2. Create a directory with a file inside it
"""

import os
new_folder = os.path.join(os.getcwd(), "Homework/FunctionsAndModules/homework_dir")
os.mkdir(new_folder)
with open(os.path.join(new_folder, "new_file.txt"), "w") as f:
    f.write('Oh Hi Mark')

"""
3. Print factorial and square of a number
"""

import math
print(math.factorial(9), math.sqrt(9))

"""
4. Return path of a specific file
"""

"""
5. Print random integer between 0 and 5
"""

import random
print(random.randint(0,5))

"""
6. Print current datetime
"""

import datetime
print(datetime.datetime.now())

"""
7. Print current time
"""

import datetime 
print(datetime.datetime.now().time())

"""
8. Converts a number of seconds to a date
"""

from datetime import datetime
seconds = 12351236123
print(datetime.fromtimestamp(seconds).strftime("%A, %B %d, %Y %I:%M:%S"))

"""
9. Print the value of pi
"""

import math
print(math.pi)

"""
10. Create your own module and import it in another python file
"""
from FunctionsAndModules.homework_dir import new_module

new_module.oh_hi_mark()

