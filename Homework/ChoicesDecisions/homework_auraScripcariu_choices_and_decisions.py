"""
1. Write a program that finds all numbers which are divisible by 7 and multiples of 5,
between 1500 and 2700 (both included). 
Then accept a number from the user and verify if it is part of the found list numbers.
Hint: use methods range(), input(), append(), try-except
"""

all_numbers = []

for number in range(1500, 2701):
    if (number % 7 == 0) and (number % 5 == 0):
        all_numbers.append(number)

# print(all_numbers)

for number in all_numbers:
    try:
        user_input = int(
            input("Please insert a number between 1500 and 2700 (both included): ")
        )
        if (
            (user_input >= 1500)
            and (user_input <= 2700)
            and (user_input in all_numbers)
        ):
            print("Your number is divisible by 7 and multiple of 5")
        elif (user_input < 1500) or (user_input > 2700):
            print("Your number is not in the specified range. Please try again.")
        elif (
            (user_input >= 1500)
            and (user_input <= 2700)
            and (user_input not in all_numbers)
        ):
            print("Your number is not divisible by 7 and multiple of 5")
    except ValueError:
        print("Error: You did not enter a number, try again")
    else:
        break


"""
2. Write a program that accepts a word from the user and print it in reverse.  
Catch any errors from user's input.
Hint: use methods range(), input(), try-except
"""

while True:
    try:
        user_word = input("Please insert a word: ")
        int(user_word)
        print("Ooops! Not a word, try again")
    except ValueError:
        print("This is a word!Let's see if is valid to reverse ... ")
        if not user_word:
            print("oops! Input should not be empty! Try again")
            continue
        elif " " in user_word:
            print("Ooops! Only 1 word without spaces is allowed! Try again")
            continue
        else:
            for i in range(len(user_word) - 1, -1, -1):
                print(user_word[i], end="")
            break
