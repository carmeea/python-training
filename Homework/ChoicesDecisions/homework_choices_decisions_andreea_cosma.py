#1

numbers = []
for num in range(1500, 2701):
    if num % 7 == 0 and num % 5 == 0:
        numbers.append(num)

print("Numbers divisible by 7 and multiplies of 5 between 1500 and 2700:")
print(numbers)

user_number = int(input("Enter a number for to ssee if it's in my list: "))
if user_number in numbers:
    print(f"{user_number} it's not in list")
else:
    raise Exception(f"{user_number} it's not in my list")


#2

word = input("Enter a name:")
reversed_word = word[::-1]
print("Reversed word:", reversed_word)