# Tic Tac Toe game

def print_board(board):
    """Prints the current state of the game board."""
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board, player):
    """Checks if the given player has won."""
    # Check rows, columns, and diagonals for a winning combination
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def is_board_full(board):
    """Checks if the board is full."""
    return all([cell != " " for row in board for cell in row])

def play_game():
    """Main function to play Tic Tac Toe."""
    # Initialize the game board
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")
        
        # Get the player's move
        try:
            row, col = map(int, input("Enter row and column (1-3 for each, separated by space): ").split())
        except ValueError:
            print("Invalid input. Please enter two numbers.")
            continue
        
        # Adjust for 0-indexed board
        row -= 1
        col -= 1
        
        # Check if the move is valid
        if row < 0 or row >= 3 or col < 0 or col >= 3 or board[row][col] != " ":
            print("Invalid move. Try again.")
            continue
        
        # Place the player's mark on the board
        board[row][col] = current_player
        
        # Check if the current player has won
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check if the game is a draw
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch to the other player
        current_player = "O" if current_player == "X" else "X"

# Start the game
play_game()
