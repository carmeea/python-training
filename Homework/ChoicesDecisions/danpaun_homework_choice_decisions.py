"""
1. Write a program that finds all numbers which are divisible by 7 and multiples of 5,
between 1500 and 2700 (both included). 
Then accept a number from the user and verify if it is part of the found list numbers.
Hint: use methods range(), input(), append(), try-except
"""

# Find all numbers divisible by 7 and multiples of 5 between 1500 and 2700
gold_numbers = []
for num in range(1500, 2701):
    if num % 7 == 0 and num % 5 == 0:
        gold_numbers.append(num)


try:
    user_num = int(input("Enter a number to check if it's in the list: "))
   
    if user_num in gold_numbers:
        print(f"{user_num} is divisible by 7 and a multiple of 5.")
    else:
        print(f"{user_num} is not divisible by 7 and a multiple of 5.")
except ValueError:
    print("Please enter a valid integer.")




"""
2. Write a program that accepts a word from the user and print it in reverse. 
Catch any errors from user's input.
Hint: use methods range(), input(), try-except
"""

def reverse_word():
    try:
        word = input("Enter a word: ")
        reversed_word = ""
        for i in range(len(word) - 1, -1, -1):
            reversed_word += word[i]
        print("Reversed word:", reversed_word)
    except Exception as e:
        print("Error:", e)

reverse_word()


