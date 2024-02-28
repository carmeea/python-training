"""
1. Write a program that finds all numbers which are divisible by 7 and multiples of 5,
between 1500 and 2700 (both included). 
Then accept a number from the user and verify if it is part of the found list numbers.
Hint: use methods range(), input(), append(), try-except
"""

numbers = []
for num in range(1500, 2701):
    if num % 7 == 0 and num % 5:
        numbers.append(num)

try:
    input = int(input("Enter number: "))
    input_number = int(input)
    if input_number in numbers:
        print("Number is divisible by 7 and is a multiple of 5")
    elif input <= 1500 or input >= 2700:
        print("Number is outside of the range!")
    else:
        print("Not dividable by 7 and is a multiple of 5")
except ValueError:
    print("Invalid input, please enter an Integer Number")

"""
2. Write a program that accepts a word from the user and print it in reverse. 
Catch any errors from user's input.
Hint: use methods range(), input(), try-except
"""

try:
    word = input("Enter a word to reverse it: ")
    if not word.isalpha():
        raise ValueError("Not a word Dummy!")
    reversed_word = word[::-1]
    print("Reversed it look like: ", reversed_word)
except ValueError:
    print("Something went wrong..")
