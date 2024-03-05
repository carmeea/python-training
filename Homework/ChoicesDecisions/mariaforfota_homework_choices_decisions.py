"""
1. Write a program that finds all numbers which are divisible by 7 and multiples of 5,
between 1500 and 2700 (both included). 
Then accept a number from the user and verify if it is part of the found list numbers.
Hint: use methods range(), input(), append(), try-except


numberList = []
for x in range(1500, 2700):
    if x % 7 == 0 and x % 5 == 0:
        numberList.append(x)

try:
    userInput = int(input("Enter a number:"))
    if userInput in numberList:
        print(f"{userInput} is in the number list!")
    else:
        print(f"{userInput} is not in the number list")
except ValueError:
    print("Enter a valid number")
"""

"""
2. Write a program that accepts a word from the user and print it in reverse. 
Catch any errors from user's input.
Hint: use methods range(), input(), try-except
"""


def reverseWord(word):
    return word[::-1]


try:
    inputWord = input("Enter a word: ")
    reversedWord = reverseWord(inputWord)
    print(f"The reversed word {inputWord} is {reversedWord}")

except Exception as e:
    print("An error occurred", e)
