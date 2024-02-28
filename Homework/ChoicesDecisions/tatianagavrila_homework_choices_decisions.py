"""
1. Write a program that finds all numbers which are divisible by 7 and multiples of 5,
between 1500 and 2700 (both included). 
Then accept a number from the user and verify if it is part of the found list numbers.
Hint: use methods range(), input(), append(), try-except
"""



# Find numbers divisible by 7 and multiples of 5 between 1500 and 2700 (inclusive)
numbers_list = [num for num in range(1500, 2701) if num % 7 == 0 and num % 5 == 0]

# Print the list of numbers
print("Numbers divisible by 7 and multiples of 5 between 1500 and 2700:", numbers_list)

# Accept a number from the user
try:
    user_number = int(input("Enter a number to check if it is in the list: "))
    
    # Verify if the user's number is in the list
    if user_number in numbers_list:
        print(f"{user_number} is part of the found list.")
    else:
        print(f"{user_number} is not part of the found list.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")


"""
2. Write a program that accepts a word from the user and print it in reverse. 
Catch any errors from user's input.
Hint: use methods range(), input(), try-except
"""

# Accept a word from the user and print it in reverse
try:
    user_word = input("Enter a word: ")
    
    # Reverse the word and print it
    reversed_word = user_word[::-1]
    print("Reversed word:", reversed_word)
except Exception as e:
    print(f"Error: {e}")
