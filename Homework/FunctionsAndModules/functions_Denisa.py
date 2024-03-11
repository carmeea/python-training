"""
1. Create a function which prints first 10 natural numbers
"""

def natural_numbers():
    list=[]
    for i in range (1,11):
        list.append(i)
    print (list)
natural_numbers()

"""
2. Create a function which prints sum of all numbers from 1 to a given number (e.g. print sum of all numbers from 1 to 5)
"""
def sum():
    total=0
    for x in range(1,6):
        total+=x
    print(total)
sum()

"""
3. Create a function with 3 arguments and return average only if is greater than 0
"""
def average_function(a,b,c):
    total=a+b+c
    average=total/3
    if average > 0:
        print("Average:",average)
    else:
        pass
    
average_function(1,2,3)
average_function(0,0,0)

"""
4. Create a function with a default argument value
"""
def hello(name="world"):
    print("Hello",name,"!")
hello()
hello("Denisa")

"""
5. Create a function which accepts 3 values and return the maximum value
"""
def max_value(a,b,c):
    list=[a,b,c]
    return max(list)

print(max(4,9,3))
