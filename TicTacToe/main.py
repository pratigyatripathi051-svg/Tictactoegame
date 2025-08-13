def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
    return any(all(cell == player for cell in row) for row in board) or \
           any(all(row[i] == player for row in board) for i in range(3)) or \
           all(board[i][i] == player for i in range(3)) or \
           all(board[i][2-i] == player for i in range(3))

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    players = ["X", "O"]
    for turn in range(9):
        print_board(board)
        player = players[turn % 2]
        print(f"Player {player}'s turn.")
        while True:
            try:
                r, c = map(int, input("Enter row and column (0-2): ").split())
                if board[r][c] == " ":
                    board[r][c] = player
                    break
                else:
                    print("Cell already taken!")
            except:
                print("Invalid input, try again.")
        if check_win(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            return
    print_board(board)
    print("It's a draw!")

tic_tac_toe()

