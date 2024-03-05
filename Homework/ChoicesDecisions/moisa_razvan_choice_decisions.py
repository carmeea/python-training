"""
1. Write a program that finds all numbers which are divisible by 7 and multiples of 5,
between 1500 and 2700 (both included). 
Then accept a number from the user and verify if it is part of the found list numbers.
Hint: use methods range(), input(), append(), try-except
"""

def is_number_included():
    number = int(input('Please write a number: '))
    if number <1500 or number> 2700:
        raise Exception(f"Sorry, but {number} is not between 1500 and 2700")
    
    numbers_divisible_by_7 = []
    for i in range(1500, 2701, 5):
        if i % 7 ==0:
            numbers_divisible_by_7.append(i)

    if number in numbers_divisible_by_7:
        print(f"{number} is part of the list")
    else:
        print(f"{number} doesn't belong to the list")

is_number_included()

"""
2. Write a program that accepts a word from the user and print it in reverse. 
Catch any errors from user's input.
Hint: use methods range(), input(), try-except
"""

def reverse_word():
    word = input("Please enter a word: ")
    print(word[::-1])

reverse_word()