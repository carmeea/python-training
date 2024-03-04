"""
1. Write a program that finds all numbers which are divisible by 7 and multiples of 5,
between 1500 and 2700 (both included). 
Then accept a number from the user and verify if it is part of the found list numbers.
Hint: use methods range(), input(), append(), try-except

"""

def find_numbers()
    result = []
    for number in range(1500, 2701):
        if number % 7 == 0 and number % 5 == 0:
                result.append(number)
    return result

divisible_by_7_and_multiple_of_5 = find_numbers()
print("Numbers divisible by 7 and multiple of 6=5 between 1500 and 2700:", divisible_by_7_and_multiple_of_5)

try:
    user_input = int(input("Enter a number to check if it is in the list: "))
    if user_input in divisible_by_7_and_multiple_of_5:
         print(f"{user_input} is in the list")
    else:
         print(f"{user_input} is not in the list")
except ValueError:
     print("Invalid input. Please enter a valid integer")



"""
2. Write a program that accepts a word from the user and print it in reverse. 
Catch any errors from user's input.
Hint: use methods range(), input(), try-except
"""
try:
     user_input = input("Enter a word: ")
     reversed_word = user_input[::-1]
     print("Reversed word:", reversed_word)
except Exception as e:
     print(f"Error: {e}")
