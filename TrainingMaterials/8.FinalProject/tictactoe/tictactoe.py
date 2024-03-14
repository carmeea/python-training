"""
Create a friendly beginner tic-tac-toe game, playing agaist computer.

Board will look like this
 | | 
-+-+-
 | | 
-+-+-
 | | 
 
Implementation Hints:
-print the game board
-take player input
-check win or tie
-switch player with computer
"""

import random

board = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}
player = "O"
computer = "X"


# Printing the game board
def printBoard(board):
    print(board[1] + "|" + board[2] + "|" + board[3])
    print("-+-+-")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-+-+-")
    print(board[7] + "|" + board[8] + "|" + board[9])
    print("\n")


# Check if position is Free
def spaceIsFree(position):
    if board[position] == " ":
        return True
    return False


# Insert Value and Check if Draw or Win
def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)
        if checkDraw():
            print("It's a Draw!")
            exit()
        if checkWin():
            if letter == "X":
                print("Computer wins! Better luck next time!")
                exit()
            else:
                print("You Win! Congrats! ;) ")
                exit()
        return
    else:
        print("Invalid position!")
        position = int(input("Please enter a new position: "))
        insertLetter(letter, position)
        return


# Check Win
def checkWin():
    # Check Row1 Win
    if board[1] == board[2] and board[1] == board[3] and board[1] != " ":
        return True
    # Check Row2 Win
    elif board[4] == board[5] and board[4] == board[6] and board[4] != " ":
        return True
    # Check Row3 Win
    elif board[7] == board[8] and board[7] == board[9] and board[7] != " ":
        return True
    # Check Column1 Win
    elif board[1] == board[4] and board[1] == board[7] and board[1] != " ":
        return True
    # Check Column2 Win
    elif board[2] == board[5] and board[2] == board[8] and board[2] != " ":
        return True
    # Check Column3 Win
    elif board[3] == board[6] and board[3] == board[9] and board[3] != " ":
        return True
    # Check Diag1 Win
    elif board[1] == board[5] and board[1] == board[9] and board[1] != " ":
        return True
    # Check Diag2 Win
    elif board[7] == board[5] and board[7] == board[3] and board[7] != " ":
        return True
    else:
        return False


# Check Draw - if any space left, game will continue
def checkDraw():
    for key in board.keys():
        if board[key] == " ":
            return False
    return True


# Take player input
def playerMove():
    position = int(input("Enter a position for 'O': "))
    insertLetter(player, position)
    return


# Switch the player to computer
def computerMove():
    print("Computer's move:")
    freePositionList = computerCheckFreePositions(board)
    if len(freePositionList) > 0:
        position = random.choice(freePositionList)
        insertLetter(computer, position)
    return


# Computer checks free position and randomnly selects position
def computerCheckFreePositions(board):
    keyList = []
    for key in board.keys():
        if spaceIsFree(key):
            keyList.append(key)
    return keyList


# Main Game play
while not checkWin():
    print("Game Start! \n")
    printBoard(board)
    computerMove()
    playerMove()
