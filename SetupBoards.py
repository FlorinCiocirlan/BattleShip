
#name_player1 = str (input ("What is your name player 1?: ") )
#name_player2 = str (input ("What is your name player 2?: ") )

import pprint

def show_boards():
    board1 = [[0 for x in range(10)] for y in range(10)] 
    pprint.pprint(board1)
    print("\n")
    board2 = [[0 for x in range(10)] for y in range(10)] 
    pprint.pprint(board2)
show_boards()
