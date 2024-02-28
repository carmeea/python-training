"""
1. Write a program that finds all numbers which are divisible by 7 and multiples of 5,
between 1500 and 2700 (both included). 
Then accept a number from the user and verify if it is part of the found list numbers.
Hint: use methods range(), input(), append(), try-except
"""

numberList=[]

for x in range(1500,2700):
    if x%5==0 and x%7==0:
        numberList.append(x)

print("Numbers between 1500 and 2700 that are multiples of 7 and divisible by 5 are", numberList, "\n")

try: 
    userInput= int(input("Enter a number: "))
except ValueError:
        print("Error: You did not enter a number")
else: 
     if userInput in numberList:
          print("Number is in the list")
     else: 
        print("Number is not in the list")

"""
2. Write a program that accepts a word from the user and print it in reverse. 
Catch any errors from user's input.
Hint: use methods range(), input(), try-except
"""
#easy version
word = input("Enter a word: ")

if word.isalpha():
    print("Inverted word is ",word[::-1],"\n")
else: 
    print("Wrong characters inserted")


#not working version

try:
    word = input("Enter a word: ")
    if word.isalpha():
         print("Inverted word is ",word[::-1])
    else: 
         print("Numbers inserted")
except Exception as e:
        print("Wrong characters inserted")
