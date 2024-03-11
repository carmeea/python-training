"""
1. Print your current working directory
"""
import os
def current_directory():
    current_dir=os.getcwd()
    print("Current working directory is:",current_dir)
    
current_directory()

"""
2. Create a directory with a file inside it
"""

"""

3. Print factorial and square of a number
"""
import math

x=6
factorial=math.factorial(x)
square=math.pow(x,2)
print("The factorial of 6 is",factorial,"and the square of 6 is",square)

"""
4. Return path of a specific file
"""
import os
print("The path is",os.path.abspath("homework_modules.py"))

"""
5. Print random integer between 0 and 5
"""
import random
rand=random.randint(0,10)
print(rand)

"""
6. Print current datetime
"""
from datetime import datetime
current_date=datetime.now()
print(current_date)

"""
7. Print current time
"""
from datetime import datetime
current=datetime.now()
current_time=current.time()
print(current_time)

"""
8. Converts a number of seconds to a date
"""
from datetime import datetime

timestamp_sec = 1710116280
date = datetime.fromtimestamp(timestamp_sec)
print(date)

"""
9. Print the value of pi
"""
import math
print(math.pi)
"""
10. Create your own module and import it in another python file
"""
