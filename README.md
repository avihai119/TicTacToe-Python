# TicTacToe-Python

This is a simple command-line implementation of the classic TicTacToe game written in Python. It allows two players to play the game in the terminal, taking turns to place their markers (X or O) on the board.

## Features

- Two-player mode
- Randomly chooses which player goes first
- Allows players to choose their marker (X or O)
- Checks for a winner or a tie
- Prompts players to play again after the game ends

## How to Play

1. Clone the repository to your local machine.
    ```bash
    git clone https://github.com/avihai119/TicTacToe-Python.git
    cd TicTacToe-Python
    ```

2. Run the script.
    ```bash
    python tictactoe.py
    ```

3. Follow the prompts to play the game:
    - The game will randomly select which player goes first.
    - The chosen player will select their marker (X or O).
    - Players take turns entering their move by selecting a number from 1 to 9 corresponding to the position on the board.
    - The game will check for a winner or a tie after each move.
    - After the game ends, players will be prompted to play again.

## Code Explanation

### Main Functions

- `choose_first()`: Randomly selects which player goes first.
- `player_mark_choice(first_player)`: Allows the first player to choose their marker (X or O).
- `pos_choice(player)`: Prompts the player to choose a position on the board.
- `place_marker(board, marker, position)`: Places the player's marker on the board at the chosen position.
- `is_game_won(board, player)`: Checks if the specified player has won the game.
- `is_board_full(board)`: Checks if the board is full.
- `replay()`: Asks the players if they want to play again.
- `display_board(board)`: Displays the current state of the board.

### Main Game Loop

The main game loop initializes the game board and controls the flow of the game, alternating turns between the two players and checking for a winner or a tie after each move.

## Example

Welcome to Tic-Tac-Toe!

player 1 is first

player 1 , please choose X or O: X

Player 1 Please choose a number (1-9): 5

| |
|X|
| |

Player 2 Please choose a number (1-9): 1

O| |
|X|
| |

...
Player 1 won!

Do you want to play again? (Y/N): N

Thanks for playing!
