
#name_player1 = str (input ("What is your name player 1?: ") )
#name_player2 = str (input ("What is your name player 2?: ") )

board=[]
for columns in range(10):
    board.append("-" * 10)

def print_board(board):
    for rows in board:
        print("  ".join(rows))

print_board(board)