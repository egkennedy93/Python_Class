####tic_tac_toe Project
#By: Everett Kennedy
#10/29/2018

import os
import random
######## Prompt player if they want to be X or O ###################


def player_input():
    while True:
        play1_input = input("Player 1: Do you want to be X or O?\n").upper()
        if play1_input == "X" or play1_input == "O":
            print(f"Player 1 selected: \"{play1_input}\"")
            print(choose_first())
            return False
        else:
            print("Incorrect option. Please enter \"X\" or \"O\"\n ")
            return True


def place_marker(board, marker, position):
    tmp_list = board
    tmp_list.insert(position, marker)
    return


def game_board(board):
    print('   ' + " | " + '  ' + "| " + '   ')
    print('  '+ board[7] + " | " +  board[8] +" | " + board[9])
    print('   ' + " | " + '  ' + "| " + '   ')
    print(' '+ "-" * 10)
    print('   ' + " | " + '  ' + "| " + '   ')
    print('  '+ board[4] + " | " +  board[5] +" | " + board[6])
    print('   ' + " | " + '  ' + "| " + '   ')
    print(' '+ "-" * 10)
    print('   ' + " | " + '  ' + "| " + '   ')
    print('  '+ board[1] + " | " +  board[2] +" | " + board[3])
    print('   ' + " | " + '  ' + "| " + '   ')
    return


def win_check(board, mark):
    if board[1:3] == mark or board[4:6] == mark or board[7:9] == mark:
        print("{} wins!".format(mark))
        return True
    elif board[1] == mark  and board[5] == mark and board[9] == mark:
        print("{} wins!".format(mark))
        return True
    elif board[3] == mark and board[5] == mark and board[7] == mark:
        print("{} wins!".format(mark))
        return True
    elif board[1] == mark and board[4] == mark and board[7] == mark:
        print("{} wins!".format(mark))
        return True
    elif board[2] == mark and board[5] == mark and board[8] == mark:
        print("{} wins!".format(mark))
        return True
    elif board[3] == mark and board[6] == mark and board[9] == mark:
        print("{} wins!".format(mark))
        return True
    else:
        return False


def space_check(board, position):
    if board[position] == ' ':
        return True
    else:
        print("That spot is already taken")
        return False


def full_board_check(board):
    for i in board:
        if i == ' ':
            return False
        else:
            return True


def player_choice(board):





def replay():
    play_again = input("Would you like to play again? Y|N").upper()
    if play_again == "Y":
        print("playing again")
        return True
    else:
        print("Thanks for playing")
        return False


def choose_first():
    choose = random.randint(1,10)
    if choose % 2 == 0:
        return "Player one has been selected to go first!"
    else:
        return "Player two has been selected to go first"


#This is function selects what letter Player 1 wants to be, and if he's ready to start
#player_input()
#test_board = ['#','X','O','X','O','X','O','X','O','X']
#place_marker(test_board, "%", 7)


print("Welcome to Tic Tac Toe!\n")
player_input()
prompt_play = input("Are you ready to play? Enter Yes or No.\n").upper()
board_list = ["#", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

if prompt_play == "YES":
    while True:
        game_board(board_list)
        win_check(board_list,"X")
elif prompt_play == "NO":
    print("Exiting...")
    exit()




####### Prompt player if they are ready to play y/n ####################

### |  | ###
### |  | ###
### |  | ###
#----------#
### |  | ###
### |  | ###
### |  | ###
#----------#
### |  | ###
### |  | ###
### |  | ###