# Write a program that finds all numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included). 
# Then accept a number from the user and verify if it is part of the found list numbers.
# Hint: use methods range(), input(), append(), try-except
x = []
for i in range (1500,2701):
    if i %7==0 and i%5==0:
        x.append(i)
print("Numbers divisible by 7 and multiplies of 5 between 1500 and 2700 are "+str(x))
inputNumber=int(input("Enter a number:"))
if inputNumber in range(1500,2701):
    print(f"{inputNumber} is in range of 1500-2700.")
else:
    print(f"{inputNumber} is not in range of 1500-2700.")
###
###
###
# Write a program that accepts a word from the user and print it in reverse. 
# Catch any errors from user's input.
# Hint: use methods range(), input(), try-except
inputWord = input("Enter a word:")
if inputWord:
    reversePrint = inputWord[::-1]
if not inputWord.isalpha():
    print("ERROR! Only A-Z, a-z letters are allowed! Spaces and special characters are forbidden!")
print("Your word spelled backwards is: ", reversePrint)