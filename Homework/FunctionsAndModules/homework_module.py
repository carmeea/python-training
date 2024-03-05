"""9. Define a function that checks if a given number is a prime number​
"""
def is_prime(x):
    for i in range(2, int(x)+1):
        if int(x) % i == 0:
                return False
        return True
        
# user_input=input("give me a number for the check ")
# if is_prime(user_input) and (int(user_input)>1):
#      print("is prime")
# else:
#      print("not prime")


"""
16. Calculate the length of a string and return that value
"""
def lung(x):
    lungime=0
    for i in x:
        lungime+=1
    