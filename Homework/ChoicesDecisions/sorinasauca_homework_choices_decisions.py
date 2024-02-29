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

numbers_list = []
for x in range (1500,2701):
    if x % 7 == 0 and x % 5 == 0:
        numbers_list.append(x)

try:
    input_nr = int (input("Enter a number: "))
    if input_nr in numbers_list:
        print(f"{input_nr} is divisible by 7 and multiple of 5")
    else: 
        print(f"{input_nr} is not divisible by 7 and multiple of 5")
except ValueError:
    print("Enter another number")

#2


def reverse_word(word):
    return word[::-1]

try:
    input_word = input ("Enter a word: ")
    reserved_word = reverse_word(input_word)
    print(f"The reserved word of {input_word} is {reserved_word}")
except Exception as e:
    print("error!")