# =========================
# Tic Tac Toe (2 players)
# =========================

def create_board():
    """Step 1: make a 3x3 grid of spaces (empty cells)."""
    return [[' ' for _ in range(3)] for _ in range(3)]


def display_board(board):
    """Step 2: print the board with row/column labels."""
    print("\n   1   2   3")
    for i, row in enumerate(board, start=1):
        print(f"{i}  " + " | ".join(row))
        if i < 3:
            print("  ---+---+---")
    print()  # blank line for spacing


def player_input(player, board):
    """
    Step 3: ask the current player for a move.
    Input format: two numbers 'row col' (each 1..3).
    Validates range + cell emptiness.
    """
    while True:
        raw = input(f"Player {player}, enter your move as 'row col' (e.g., 2 3), or 'q' to quit: ").strip()
        if raw.lower() in ("q", "quit", "exit"):
            print("Game exited.")
            raise SystemExit

        parts = raw.split()
        if len(parts) != 2:
            print("Please enter exactly two numbers, like: 2 3")
            continue

        try:
            r, c = int(parts[0]), int(parts[1])
        except ValueError:
            print("Both row and column must be numbers (1 to 3).")
            continue

        if not (1 <= r <= 3 and 1 <= c <= 3):
            print("Row and column must be between 1 and 3.")
            continue

        # Convert to 0-based indexes
        r_idx, c_idx = r - 1, c - 1

        if board[r_idx][c_idx] != ' ':
            print("That cell is already taken. Choose another.")
            continue

        return r_idx, c_idx


def check_win(board, player):
    """Step 4: True if 'player' has 3 in a row (row, column, or diagonal)."""
    # Rows
    for r in range(3):
        if all(board[r][c] == player for c in range(3)):
            return True
    # Columns
    for c in range(3):
        if all(board[r][c] == player for r in range(3)):
            return True
    # Diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def board_full(board):
    """Step 5: True if there are no spaces left."""
    return all(cell != ' ' for row in board for cell in row)


def switch_player(player):
    """Helper: swap 'X' <-> 'O'."""
    return 'O' if player == 'X' else 'X'


def play():
    """Step 6: main game loop."""
    board = create_board()
    current = 'X'  # X always starts

    print("Welcome to Tic Tac Toe! Player X starts.")
    while True:
        display_board(board)

        # Get a legal move from the current player
        r, c = player_input(current, board)
        board[r][c] = current

        # Check for win
        if check_win(board, current):
            display_board(board)
            print(f"🎉 Player {current} wins! 🎉")
            break

        # Check for tie
        if board_full(board):
            display_board(board)
            print("It's a tie! 🤝")
            break

        # Switch to the other player
        current = switch_player(current)


# Run the game
if __name__ == "__main__":
    play()