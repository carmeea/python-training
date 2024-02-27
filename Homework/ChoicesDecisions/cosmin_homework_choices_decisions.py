"""
1. Write a program that finds all numbers which are divisible by 7 and multiples of 5,
between 1500 and 2700 (both included). 
Then accept a number from the user and verify if it is part of the found list numbers.
Hint: use methods range(), input(), append(), try-except
"""


list = []
for x in range(1500, 2701):
    if x % 7 == 0 and x % 5 == 0:
        list.append(x)
    
print(list)

try:
    user_number = int(input("Enter a number between 1500 and 2700 to check if it is in the list: "))
    if user_number in list:
        print(f"{user_number} is in the list!")
    else: 
        print(f"{user_number} is not in the list!")
except ValueError:
    print("Please enter a valid number!")


"""
2. Write a program that accepts a word from the user and print it in reverse. 
Catch any errors from user's input.
Hint: use methods range(), input(), try-except
"""

try:
    word = input("Enter a word or a sentence: ")
    if word.lstrip("-").isdigit():
        raise ValueError("Input should not be a number!")
    if not word:
        raise ValueError("Input should not be empty!")
    if word.isspace():
        raise ValueError("Input should not be whitespaces!")
    reversed_word = ''
    for i in range(len(word)-1, -1, -1):
        reversed_word += word[i]
    print("Reversed word or sentence:", reversed_word)
except ValueError as ve:
    print(ve)
except Exception as e:
    print("An error occurred:", e)