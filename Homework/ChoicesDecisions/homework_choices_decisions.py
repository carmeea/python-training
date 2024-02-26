"""
1. Write a program that finds all numbers which are divisible by 7 and multiples of 5,
between 1500 and 2700 (both included). 
Then accept a number from the user and verify if it is part of the found list numbers.
Hint: use methods range(), input(), append(), try-except


2. Write a program that accepts a word from the user and print it in reverse. 
Catch any errors from user's input.
Hint: use methods range(), input(), try-except
"""

#1
results = []
for i in range(1500, 2700, 5):
    if i % 7 == 0:
        results.append(i)

print(results)

user_input = input("give me an integer to check wether it is in the results list\n")

try:
    if int(user_input) in results:
        print("Number given is in the result list")
    else:
        print("number not in list")
except ValueError:
    print("Invalid input. Please try again")

#2.1
user_word = input("give me an english word for printing it out in reverse\n")
letters_list=list(user_word)
#print(letters_list)
reversed_word = ""

try:
    if user_word.isalpha():
       letters_list.reverse()
       #print(letters_list)
       for i in range(len(user_word)):
           reversed_word = reversed_word + letters_list[i]
       print(reversed_word)
    else:
        print("given input is not a word in english")
except ValueError:
    print["Invalid input.Please try again"]
        