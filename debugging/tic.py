def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if all(cell == row[0] and cell != " " for cell in row):
            return True

    for col in range(len(board[0])):
        if all(board[row][col] == board[row + 1][col] == board[row + 2][col] and board[row][col] != " " for row in range(len(board) - 2)):
            return True

    if all(board[i][i] == board[i + 1][i + 1] and board[i][i] != " " for i in range(len(board) - 1)):
        return True

    if all(board[i][len(board) - i - 1] == board[i + 1][len(board) - i - 2] and board[i][len(board) - i - 1] != " " for i in range(len(board) - 1)):
        return True

    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while not check_winner(board):
        print_board(board)
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            if board[row][col] == " ":
                board[row][col] = player
                player = "O" if player == "X" else "X"
            else:
                print("That spot is already taken! Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter valid row and column numbers.")

    print_board(board)
    print("Player " + player + " wins!")

tic_tac_toe()
