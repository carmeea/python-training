import os, math, random, datetime
#from homework_functions import lungime
"""
1. Print your current working directory
"""
print(os.getcwd())

"""
2. Create a directory with a file inside it
"""
os.mkdir('/home/p3/ws24/python-training/ceva')
with open('/home/p3/ws24/python-training/ceva/myfile.txt',"w") as fp:
    pass

"""
3. Print factorial and square of a number
"""
print("give me a number to calculate factorial and square\n")
x=input()
print(f" factorial is {math.factorial(int(x))}\n square is {math.sqrt(int(x))}")

"""
4. Return path of a specific file
"""
print("Path of file is ", os.path.abspath("myfile.txt"))
"""
5. Print random integer between 0 and 5
"""
print(f"random number between 0 and 5 is {random.randint(0,5)}")
"""
6. Print current datetime
"""
today = datetime.datetime.now()
print(f"time and date right now is {today}")
"""
7. Print current time
"""
print(f"time right now is: {today.strftime('%H:%M:%S')}")
"""
8. Converts a number of seconds to a date
"""
seconds_input=input("give me a number of seconds to convert them to a date\n")
print(datetime.timedelta(seconds=int(seconds_input)))
"""
9. Print the value of pi
"""
print(f"Pi is: {math.pi}")

"""
10. Create your own module and import it in another python file
"""
user_input=input("Give me a word for counting it's length:\n")
print(f"length of given word is: {lungime(user_input)}")