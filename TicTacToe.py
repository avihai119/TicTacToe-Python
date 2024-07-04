import random

# Function to randomly choose which player goes first
def choose_first():
    rand_num = random.randint(1,2)
    if rand_num == 1:
        return 'player 1'
    else:
        return 'player 2'

# Function to allow the first player to choose their marker (X or O)
def player_mark_choice(first_player):
    mark = ''
    while (mark != 'X' and mark != 'O'): # Infinite loop to make sure players choose X or O
        mark = input('{} , please choose X or O: '.format(first_player))
    if first_player == 'player 1':
        player1 = mark
        player2 = 'O' if player1 == 'X' else 'X'
    else:
        if first_player == 'player 2':
            player2 = mark
            player1 = 'O' if player2 == 'X' else 'X'

    return (player1,player2)

# Function to prompt the player to choose a position on the board
def pos_choice(player):
    while True:
        try:
            choice = int(input('{} Please choose a number (1-9):'.format(player)))
            if 1 <= choice <= 9:
                return choice
            else:
                print('Number is out of range, please choose again')
        except:
            print('Invalid input, please enter a number (1-9)')

# Function to place the marker on the board
def place_marker(board,marker,position):
    while board[position] != '' or board[position] == '#' : # Checking if the position is valid
        print('Position is out of range or already picked!')
        position = int(input('Please enter a number (1-9):'))
    board[position] = marker
    return board

# Function to check if a player has won the game
def is_game_won(board,player):
    mark = player
    # Checking for each combination to see if player won
    if board[1] == board[5] == board[9] == mark:
        return True
    elif board[3] == board[5] == board[7] == mark:
        return True
    elif (board[1] == board[2] == board[3] == mark) or (board[4] == board[5] == board[6] == mark) or (board[7] == board[8] == board[9] == mark):
        return True
    elif (board[1] == board[4] == board[7] == mark) or (board[2] == board[5] == board[8] == mark) or (board[3] == board[6] == board[9] == mark):
        return True
    else:
        return False # Player hasn't won yet

# Function to check if the board is full
def is_board_full(board):
    return all(cell != '' for cell in board[1:10])

# Function to ask if the players want to play again
def replay():
    choice =  input('Do you want to play again? (Y/N)')
    while choice != 'Y' and choice != 'N':
        print('Wrong choice, please choose Y or N')
        choice =  input('Do you want to play again? (Y/N)')
    if choice == 'Y':
        return True
    else:
        return False 

# Function to display the current state of the board
def display_board(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[7] + '|' + board[8] + '|' + board[9])

print('Welcome to Tic-Tac-Toe!')

# Main game loop
game_on = True # Variable to control the overall game loop
last_mark = '' # Variable to keep track of the last marker placed
board_full = False # Variable to check if the board is full
while game_on: 
    pos = 0
    player1 = ['', ''] # Array to store player 1's name and marker
    player2 = ['', ''] # Array to store player 2's name and marker
    player1_turn = False # Boolean to control player 1's turn
    player2_turn = False # Boolean to control player 2's turn

    # Randomly choose which player goes first
    first_player = choose_first()

    if first_player == 'player 1':
        player1[0] = first_player
        player2[0] = 'player 2'
        player1_turn = True
        player2_turn = False
    else:
        player2[0] = first_player
        player1[0] = 'player 2'
        player2_turn = True
        player1_turn = False
    print('{} is first'.format(first_player))

    # Get player markers
    player1[1], player2[1] = player_mark_choice(first_player)

    # Initialize the game board , since we are placing X or O from 1 to 9 the first place is filled with a dummy
    game_board = ['#', '', '', '', '', '', '', '', '','']
    while not is_game_won(game_board, player1[1]) and not is_game_won(game_board, player2[1]) and not board_full:
        if player1_turn:
            # Player 1's turn
            pos = pos_choice(player1[0]) # Get position choice from player 1
            game_board = place_marker(game_board, player1[1], pos) # Place marker on the board
            display_board(game_board) # Display the updated board
            last_mark = player1[1] # Update the last marker placed
            board_full = is_board_full(game_board)  # Check if the board is full
            player1_turn = False # End player 1's turn
            player2_turn = True # Start player 2's turn
        elif player2_turn:
            # Player 2's turn
            pos = pos_choice(player2[0]) # Get position choice from player 2
            game_board = place_marker(game_board, player2[1], pos) # Place marker on the board
            display_board(game_board) # Display the updated board
            last_mark = player2[1] # Update the last marker placed
            board_full = is_board_full(game_board) # Check if the board is full
            player1_turn = True # Start player 1's turn
            player2_turn = False # End player 2's turn

    if board_full and not is_game_won(game_board, player1[1]) and not is_game_won(game_board, player2[1]):
        print('The game is a tie!')
        game_on = replay() # Ask if the players want to play again
        if game_on:
            game_board = ['#', '', '', '', '', '', '', '', '',''] # Reset the game board
    else:
        # Announce the winner
        if last_mark == player1[1]:
            print('Player 1 won!')
            if game_on:
                game_board = ['#', '', '', '', '', '', '', '', '',''] # Reset the game board
        else:
            print('Player 2 won!')
            game_on = replay() # Ask if the players want to play again
            if game_on:
                game_board = ['#', '', '', '', '', '', '', '', '',''] # Reset the game board

print('Thanks for playing!') # Game Over





