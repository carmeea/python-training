"""
1. Write a program that finds all numbers which are divisible by 7 and multiples of 5,
between 1500 and 2700 (both included). 
Then accept a number from the user and verify if it is part of the found list numbers.
Hint: use methods range(), input(), append(), try-except
"""

list = []
for i in range(1500, 2700):
    if i % 7 == 0 and i % 5 == 0:
        list.append(i)
print(list)
try:
    number = int(input("Please enter a number: "))
    if number in list:
        print("Your number is in the list")
    else:
        print("Your number is not in the list")

except ValueError:
    print("Error: You did not enter a number")


"""
2. Write a program that accepts a word from the user and print it in reverse. 
Catch any errors from user's input.
Hint: use methods range(), input(), try-except
"""
try:
    word = input("Enter a word: ")
    reverse = ""
    if word.isalpha():
        for i in range(len(word)-1, -1, -1):
            print(word[i])
            reverse += word[i]
        print(reverse)
    else:
        print("Your input is not a word")
except TypeError:
    print("Invalid input")