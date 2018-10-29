####tic_tac_toe Project
#By: Everett Kennedy
#10/29/2018

import os
######## Prompt player if they want to be X or O ###################


def pick_x_o():
    print("Welcome to Tic Tac Toe!\n")
    play1_input = input("Player 1: Do you want to be X or O?\n").upper()
    while True:
        if play1_input == "X" or play1_input =="O":
            print(f"Player 1 selected: \"{play1_input}\"")
            print("Player 1 will go first\n")
            return False
        else:
            print("Incorrect option. Please enter \"X\" or \"O\"\n ")
            return True


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

#This is function selects what letter Player 1 wants to be, and if he's ready to start 
pick_x_o()

prompt_play = input("Are you ready to play? Enter Yes or No.\n").upper()
if prompt_play == "YES":
    game_board(score)
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