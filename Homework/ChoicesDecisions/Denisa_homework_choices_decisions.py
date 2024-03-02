"""
1. Write a program that finds all numbers which are divisible by 7 and multiples of 5,
between 1500 and 2700 (both included). 
Then accept a number from the user and verify if it is part of the found list numbers.
Hint: use methods range(), input(), append(), try-except
"""

numbers_list=[]

for i in range (1500,2701):
    if i%7 == 0 and i%5 == 0:
        numbers_list.append(i)
        
print (numbers_list)

try:
    user_input=int(input("Please enter a number: "))
    if user_input in numbers_list:
        print (user_input,"is part of the numbers list.")
    else:
        raise IndexError("This number isn't part of the numbers list.")
except IndexError as ie:
    print(ie)
except ValueError:
    print ("Invalid number.")
except Exception as e:
    print ("An error occured!",e)


"""
2. Write a program that accepts a word from the user and print it in reverse. 
Catch any errors from user's input.
Hint: use methods range(), input(), try-except
"""

try:
    word = input("Please enter a word: ")
    if not word:
        raise ValueError("Input cannot be empty!")
    if not word.isalpha():
        raise ValueError("Input should contain only alphabetical characters!")
    
    reverse_word=''
    for i in range(len(word)-1,-1,-1):
        reverse_word += word[i]
    print ("Reversed word:",reverse_word)

except ValueError as ve:
    print(ve)
except Exception as e:
    print("An error occured",e)