import random
import tkinter as tk
from tkinter import simpledialog
import os


# This script ask the players names
# I used Tkinter for this
# These names will be stored in the same variables as before
# These variable can be accesed as before


root = tk.Tk()
root.withdraw()

name_player1 = simpledialog.askstring(title="Start", prompt="What is your name player 1?")
name_player2 = simpledialog.askstring(title="Start", prompt="What is your name player 2?")


# This function clears the screen
# We will use this to hide the other player's table
# While is not his turn


def clear():
    os.system("clear")


clear()


# this is the board initialization as a list

board1 = []
board2 = []


# This part of the module creates the board
# Which is an 8 x 8 grid
# Every "-" element can be accesed as usually
# For example : print(board[2][2])
# Note: If we print this board now
# It will be shown as an usual list
# Example [[...],[....],[....]]


for columns in range(8):
    board1.append("-" * 8)

for columns in range(8):
    board2.append("-" * 8)

# This function prints the board without brackets
# The output will be a grid but without brackets and commas


def print_board(x):
    for rows in x:
        print("  ".join(rows))


print_board(board1)


# This function will choose who will start


players = [name_player1, name_player2]


def starting_player():
    return random.choice(players)


# This script prints who will start

if starting_player() == name_player1:
    print("%s will start the game!" % (name_player1))
elif starting_player == name_player2:
    print("%s will start the game!" % (name_player2))


# This function asks the players to
# Choose the position of their ships
