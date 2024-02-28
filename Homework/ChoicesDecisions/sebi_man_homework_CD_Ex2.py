import re

while True:
    user_input = input("Enter your word here: ")
    if not re.match("^[A-Za-z]*$", user_input):
        print("Only letters are allowed!")
    else:
        reversed_word = user_input[::-1]
        print(f"Reversed word: {reversed_word}")
        break

    
