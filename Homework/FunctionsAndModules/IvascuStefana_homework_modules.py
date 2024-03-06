#1. Print your current working directory
#%%
import os
print("Current working directory:", os.getcwd())

#2. Create a directory with a file inside it
#%%
import os
directory_name = "my_directory"
file_name = "my_file.txt"
os.makedirs(directory_name, exist_ok=True)
with open(os.path.join(directory_name, file_name), 'w') as file:
    file.write("This is a sample file.")

#3. Print factorial and square of a number
#%%
import math
number = int(input("Enter a number: "))
factorial = math.factorial(number)
square = number ** 2
print("Factorial of", number, "is:", factorial)
print("Square of", number, "is:", square)

#4. Return path of a specific file
#%%
def find_file_path(filename):
    for root, dirs, files in os.walk(os.getcwd()):
        if filename in files:
            return os.path.join(root, filename)
    return None

filename = input("Enter filename to search: ")
file_path = find_file_path(filename)
if file_path:
    print("Path of", filename, "is:", file_path)
else:
    print("File", filename, "not found.")

#5. Print random integer between 0 and 5
#%%  
import random
random_integer = random.randint(0, 5)
print("Random integer between 0 and 5:", random_integer)


#6. Print current datetime
#%%
import datetime
current_datetime = datetime.datetime.now()
print("Current datetime:", current_datetime)

#7. Print current time
#%%
import datetime
current_time = datetime.datetime.now().time()
print("Current time:", current_time)

# %%
