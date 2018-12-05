####tic_tac_toe Project
#By: Everett Kennedy
#10/29/2018

import os
import random
######## Prompt player if they want to be X or O ###################


def player_input():
    ready = True
    while ready:
        play1_input = input("Player 1: Do you want to be X or O?\n").upper()
        if play1_input == "X" or play1_input == "O":
            print(f"Player 1 selected: \"{play1_input}\"")
            print(choose_first())
            return play1_input
        else:
            print("Incorrect option. Please enter \"X\" or \"O\"\n ")
            ready = True


def place_marker(board, marker, position):
    tmp_list = board
    tmp_list.pop(position)
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
    x_win = ["X", "X", "X"]
    o_win = ["O", "O", "O"]
    if board[1:4] == x_win or board[4:7] == x_win or board[7:10] == x_win:
        print("{} wins!".format(mark))
        return True
    if board[1:4] == o_win or board[4:7] == o_win or board[7:10] == o_win:
        print("{} wins!".format(mark))
        return True
    elif board[1] == mark and board[5] == mark and board[9] == mark:
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
        if i == ' ' or i == "#":
            return False
        else:
            return True


def player_choice(board):
    choice = input("Choose your next position: (1-9)")
    if space_check(board, int(choice)) is True:
        return int(choice)

    else:
        return "That position is already taken"


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
        return "Player one has been selected to go first! \n"
    else:
        return "Player two has been selected to go first! \n"


while True:
    print("Welcome to Tic Tac Toe!\n")
    board_list = ["#", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    start_mark = player_input()
    prompt_play = input("Are you ready to play? Enter Yes or No.\n").upper()
    turn = 1
    if prompt_play == "YES":
        while full_board_check(board_list) is False:
            if turn % 2 != 0:
                play1_mark = start_mark
                game_board(board_list)
                selection = player_choice(board_list)
                place_marker(board_list, play1_mark, selection)
                print("\n" * 100)
                turn = turn + 1
                if win_check(board_list, play1_mark):
                    game_board(board_list)
                    if replay():
                        break
                    else:
                        quit()
                else:
                    continue
            elif turn % 2 == 0:
                if start_mark == "X":
                    play2_mark = "O"
                else:
                    play2_mark = "X"
                game_board(board_list)
                selection = player_choice(board_list)
                place_marker(board_list, play2_mark, selection)
                print("\n" * 100)
                turn = turn + 1
                if win_check(board_list, play2_mark):
                    game_board(board_list)
                    if replay():
                        break
                    else:
                        quit()
                else:
                    continue
