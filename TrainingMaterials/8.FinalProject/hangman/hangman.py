"""
Create a friendly beginner hangman game. It will be a simple command line game.
It will allow for user input, display a visual of current hangman state and
the word that is being guessed, every turn.

Implementation Hints:
-Get word from pre-existing word list
-User can guess a letter or a word
-Loop game play until player gives "No" as input 
-Number of tries is 6 (head, torso, 2xarms, 2xlegs)
-Output to user if letter was already entered
-Display a visual of hangman for each miss or guess.
"""

import random
from words import word_list


# Get a radomn word from the list of words and transfor to UPPERCASE letters
def get_word():
    word = random.choice(word_list)
    return word.upper()


# Display the word each turn
def play(word):
    # Display the "_" instead of word letter ex: car -> _ _ _
    # Word_completion will be updated with guessed letters
    word_completion = "_" * len(word)
    guessed = False
    # List of guessed letters
    guessed_letters = []
    # List of guessed words
    guessed_words = []
    tries = 6
    print("Let's play Hangman!")
    # Display initial state of hangman
    print(display_hangman(tries))
    # Display initial state of the word with "_"
    print(word_completion)
    print("\n")
    # Loop until the words is guessed or the user runs out of tries
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        # Guessing the letter
        if len(guess) == 1 and guess.isalpha():
            # Check if letter has been already guessed
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            # Check if letter is not in the word
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            # Check if letter is in the word
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                # Update word_completion to display it later to the user
                word_as_list = list(
                    word_completion
                )  # convert word_completion to a list to index it
                # Find all indeces where guess occurs in the word, using list comprehention
                indices = [i for i, letter in enumerate(word) if letter == guess]
                # Replace each underscore "_" with guessed letter
                for index in indices:
                    word_as_list[index] = guess
                # Convert back the list to a string
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        # Guessing the word, contains only letters
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                # User correctly guessed the word
                guessed = True
                word_completion = word
        # User types something else
        else:
            print("Not a valid guess.")
        # Print current state of the hangman
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    # Check if user guessed the word
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")


# Display visual hangman board
def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
        """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \\
                   -
                """,
        # head, torso, both arms, and one leg
        """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                   -
                """,
        # head, torso, and both arms
        """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                   -
                """,
        # head, torso, and one arm
        """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                   -
                """,
        # head and torso
        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
        # head
        """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
        # initial empty state
        """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """,
    ]
    return stages[tries]


# Logic for game play
def main():
    word = get_word()
    play(word)
    # Loop play until player gives "No" as input
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


"""
Short note: __name__ == "__main__" allows execution of code when
the file runs as a script, but not when it's imported as a module
"""
if __name__ == "__main__":
    main()
