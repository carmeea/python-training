"""
18. Assign 3 to variable glass_of_water, print "I drank 3 glasses of water today." and after that assign a new value to our variable. 
Print the result
"""


def numbers():
    number = input("How many glasses of watter did you drink today? ")
    return int(number)


def result(number):
    print(f"I drank {number} glasses of watter today.")


result(numbers())
