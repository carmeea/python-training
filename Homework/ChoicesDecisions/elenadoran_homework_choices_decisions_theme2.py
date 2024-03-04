"""
2. Write a program that accepts a word from the user and print it in reverse. 
Catch any errors from user's input.
Hint: use methods range(), input(), try-except
"""


def enter_word():
    word = input("Enter a word: ")
    return word


def reverse_word(word):
    word_reverse = ""
    index = len(word)
    try:
        while index > 0:
            word_reverse += word[index - 1]
            index = index - 1
        user_input = word
        if not user_input:
            raise ValueError("Error: You did not enter a word")
    except ValueError as e:
        print(e)
        return None
    return word_reverse


print(reverse_word(enter_word()))
