
# Problem 1
#%%
numbers = []
for num in range(1500, 2701):
    if num % 7 == 0 and num % 5 == 0:
        numbers.append(num)
print(numbers)
try:
    user_number = int(input("Enter a number to check if it is in the list: "))
    if user_number in numbers:
     print(f"{user_number} is in the list.")
    else:
        print(f"{user_number} is not in the list.")
except ValueError:
    print("Please enter a valid number.")

#2.
  #%%  
 
def is_all_letters(word):
    return word.isalpha()

def reverse_word(word):
    return word[::-1]

try:
    user_word = input("Enter a word: ")
    if not is_all_letters(user_word):
        raise ValueError("Please enter a word containing only letters.")
    
    reversed_word = reverse_word(user_word)
    print("Reversed word:", reversed_word)
except ValueError:
    print("Please enter a valid word.") 
 #%%     