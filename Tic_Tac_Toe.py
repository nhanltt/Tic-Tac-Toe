import os

# print the board of game on the screen
def display_board(board):
    os.system('cls')
    exboard = ['#','1','2','3','4','5','6','7','8','9']
    print(exboard[1] + '|' + exboard[2] + '|' + exboard[3])
    print('-+-+-')
    print(exboard[4] + '|' + exboard[5] + '|' + exboard[6])
    print('-+-+-')
    print(exboard[7] + '|' + exboard[8] + '|' + exboard[9])
    print()
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])


# Let players choose their maker 'X' or 'O'
def player_input():
    print("Please pick a maker 'X' or 'O'")
    c = False
    player = ['#', '', '']
    while c == False:
        n = input()
        if n.lower() == 'x' or n.lower() == 'o':
            c = True
        else:
            print("Please pick a maker 'X' or 'O'")
        if n == 'X':
            player[1] = 'X'
            player[2] = 'O'
        else:
            player[1] = 'O'
            player[2] = 'X'
    print(f'Player 1 is {player[1]}')
    print(f'Player 2 is {player[2]}')
    return player


# Check if the player is winner
def win_check(board, mark):
    if board[1] == board[2] == board[3] == mark or board[4] == board[5] == board[6] == mark or board[7] == board[8] == \
            board[9] == mark: return True
    if board[1] == board[4] == board[7] == mark or board[2] == board[5] == board[8] == mark or board[3] == board[6] == \
            board[9] == mark: return True
    if board[1] == board[5] == board[9] == mark or board[3] == board[5] == board[7] == mark: return True
    return False


import random


# Random who is the first player 
def choose_first():
    return random.randint(1, 2)


# Check if position is empty 
def space_check(board, position):
    return board[position] == ' '


# Check if the board remains empty position 
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


# Player choose his/her position 
def player_choice(board,name):
    n = 0
    while n not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, n):
        os.system('cls')
        display_board(board)
        print(f"Turn of player #{name}")
        n = int(input('Please choose position: (1-9) '))
    return n


# Ask the players if they want to restart a new game or exit from game 
def replay():
    s = '1'
    while (not s.lower() in 'yesno') or s.isnumeric() :
        print("Do you want to play again? Please enter 'Yes' or 'No'", end=' ')
        s = input()
    return s.lower() == 'yes'


# Welcome to game Tic Tac Toe
print('Welcome to Tic Tac Toe!')

name = 0

while True:
    # Define a empty board and let player choose maker
    board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    player = player_input()

    # Random who goes first 
    if choose_first() == 1:
        name = 1
    else:
        name = 2
    print(f'The first player is player #{name}')

    # Asking if players is already 
    start = '1'
    while (not start.lower() in 'yesno') or start.isnumeric():
        start = input('Are you ready to start game? Please enter Yes or No: ')
    if start.lower() == 'yes':
        game_on = True
    else:
        game_on = False

    # Start game 
    while game_on:

        # Print the board and get the choice of player 
        display_board(board)
        i = player_choice(board,name)
        board[i] = player[name]

        # Check if player is winner or the game is tie
        if win_check(board, player[name]) == True:
            display_board(board)
            print(f'The winner is player #{name}')
            game_on = False
        else:
            if full_board_check(board):
                display_board(board)
                print('TIE GAME!')
                game_on = False

    # Change the turn of player 
        if name % 2 == 0:
            name = 1
        else:
            name = 2

    # Asking for start a new game or exit game 
    if replay() == False:
        break
    os.system('cls')
