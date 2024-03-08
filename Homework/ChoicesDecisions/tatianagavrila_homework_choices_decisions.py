"""
1. Write a program that finds all numbers which are divisible by 7 and multiples of 5,
between 1500 and 2700 (both included). 
Then accept a number from the user and verify if it is part of the found list numbers.
Hint: use methods range(), input(), append(), try-except
"""
# Find numbers divisible by 7 and multiples of 5 between 1500 and 2700 (inclusive)
my_list = [num for num in range(1500, 2701) if num % 7 == 0 and num % 5 == 0]

# #second way
# my_list2 = []
# for num in range(1500, 2701):
#     if num % 7 == 0 and num % 5 == 0:
#         my_list2.append(num)
# Print the list of numbers
print("Numbers divisible by 7 and multiples of 5 between 1500 and 2700:", my_list)

# Accept a number from the user
try:
    user_number = int(input("Enter a number to check if it is in the list: "))
    
    # Verify if the user's number is in the list
    if user_number in my_list:
        print(f"{user_number} is part of my list.")
    else:
        print(f"{user_number} is not part of my list.")
except ValueError:
    print("Invalid input. Please try again.")


"""
2. Write a program that accepts a word from the user and print it in reverse. 
Catch any errors from user's input.
Hint: use methods range(), input(), try-except
"""

# Accept a word from the user and print it in reverse
try:
    user_word = input("Enter a word: ")
    
    # Reverse the word and print it
    reversed_1 = user_word[::-1]
    reversed_2 = ''.join(reversed(user_word))
    reversed_3 = ''
    for char in user_word:
        reversed_3 = char + reversed_3

    # Print the reversed word
    print("Reversed word1:", reversed_1)
    print("Reversed word2:", reversed_2)
    print("Reversed word3:", reversed_3)

except Exception as e:
    print(f"Error: {e}")


