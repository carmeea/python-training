number_list = [num for num in range(1500, 2701) if num % 7 == 0 and num % 5 == 0]
print("Numbers between 1500 and 2700 that are divisible by 7 and multiples of 5 are:", number_list)
number_input = int(input("Enter a number:"))
if number_input in number_list:
    print(f"{number_input} is part of the list")
else:
    print(f"{number_input} is not part of the list")



try:
    word = input("Please enter any word: ")
    if not word.isalpha():
        raise ValueError("Invalid input, please enter a valid word with letters only.")
except ValueError as e:
    print(e)
else:
    print("Word in reverse:",' '.join(reversed(word)))
