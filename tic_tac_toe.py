def print_board(board):
    print("\n")
    print("     1   2   3")
    print("   -------------")
    for idx, row in enumerate(board, start=1):
        print(f" {idx} | " + " | ".join(row) + " |")
        print("   -------------")
    print("\n")

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    return all(cell != ' ' for row in board for cell in row)

def get_move(player):
    while True:
        move = input(f"Player {player}, enter your move as row,col (e.g., 2,3): ")
        if len(move) != 3 or move[1] != ',':
            print("Invalid format. Please enter row and column as row,col (e.g., 2,3).")
            continue
        row, col = move.split(',')
        if not (row.isdigit() and col.isdigit()):
            print("Row and column must be numbers.")
            continue
        row, col = int(row), int(col)
        if not (1 <= row <= 3 and 1 <= col <= 3):
            print("Row and column must be between 1 and 3.")
            continue
        return row - 1, col - 1

def tic_tac_toe():
    print("Welcome to Tic-Tac-Toe! Let's have some fun!")
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        row, col = get_move(current_player)
        if board[row][col] != ' ':
            print("That spot is already taken. Try again.")
            continue
        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins! Congratulations! 🎉")
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw! Well played both!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

    print("Thank you for playing Tic-Tac-Toe!")

if __name__ == "__main__":
    tic_tac_toe()
