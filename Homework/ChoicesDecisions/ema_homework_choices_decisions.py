"""
1. Write a program that finds all numbers which are divisible by 7 and multiples of 5,
between 1500 and 2700 (both included). 
Then accept a number from the user and verify if it is part of the found list numbers.
Hint: use methods range(), input(), append(), try-except"""

numbers = []
for num in range(1500, 2701):
    if num % 7 == 0 and num % 5 == 0:
        numbers.append(num)
print("Numbers between 1500 and 1700 that are divisible by 5 and 7: ", numbers)

userNumber = int(input("Enter a number: "))
if userNumber in numbers:
    print(f"The number {userNumber} is part of the list ")
else:
    raise Exception(f"The number {userNumber} is not part of the list ")


"""2. Write a program that accepts a word from the user and print it in reverse. 
Catch any errors from user's input.
Hint: use methods range(), input(), try-except1
"""

word = input("Enter a word: ")
reversed_word = word[::-1]
print("The reversed word is: ", reversed_word)
