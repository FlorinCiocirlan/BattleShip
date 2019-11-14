import random
import tkinter as tk
from tkinter import simpledialog
import os


# This script ask the players names
# We used Tkinter for this
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
board_attack1 = []
board_attack2 = []


# This part of the module creates the board
# Which is an 8 x 8 grid
# Every "-" element can be accesed as usually
# For example : print(board[2][2])
# Note: If we print this board now
# It will be shown as an usual list
# Example [[...],[....],[....]]


for columns in range(8):
    board1.append(["-"] * 8)

for columns in range(8):
    board2.append(["-"] * 8)


# This function prints the board without brackets
# The output will be a grid but without brackets and commas


def print_board(x):
    print("   1  2  3  4  5  6  7  8")
    y = ["1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 "]
    for rows, i in zip(x, y):
        print(i, "  ".join(rows))


print_board(board1)


# This function will choose who will start


def choose_starting_player():
    global name_player2, name_player1
    players = [name_player1, name_player2]
    return random.choice(players)


# This script prints who will start


def print_starting_player():
    if choose_starting_player() == name_player1:
        print("%s will start the game!" % (name_player1))
    elif choose_starting_player == name_player2:
        print("%s will start the game!" % (name_player2))


# This script ask the player
# To choose where he wants to position his ship
# This also verifies if the user input positions
# Don't exceed the board


def set_position_y():
    global direction
    correct_value = True
    down_direction = True
    while correct_value is True:
        try:
            ship_y = int(input("Choose a row: "))
            assert ship_y > 0 and ship_y < 9
            correct_value = False
        except (AssertionError, ValueError):
            print("Please insert a number between 1 and 8")
    while down_direction is True and (direction == "DOWN" or direction == "down"):
        try:
            assert ship_y <= 5
            down_direction = False

        except AssertionError:
            print("Your ship won't fit on the board")
            down_direction = True
            ship_y = set_position_y()
    return ship_y


def set_position_x():
    global direction
    correct_value = True
    right_direction = True
    while correct_value is True:
        try:
            ship_x = int(input("Choose a column: "))
            assert ship_x > 0 and ship_x < 9
            correct_value = False
        except (AssertionError, ValueError):
            print("Please insert a number between 1 and 8")
    while right_direction is True and (direction == "right" or direction == "RIGHT"):
        try:
            assert ship_x <= 5
            right_direction = False

        except AssertionError:
            print("Your ship won't fit on the board")
            right_direction = True
            ship_x = set_position_x()
    return ship_x


correct_direction_values = ["right", "down", "DOWN", "RIGHT", "Right", "Down"]


def set_direction():
    correct_value = True
    while correct_value is True:
        try:
            direction = input("Choose a direction(down or right): ")
            if direction not in correct_direction_values:
                raise Exception
            else:
                correct_value = False
        except (ValueError, Exception):
            print("Please choose between right or down")
    return direction


# This script will put the ship on the board
# Y is the height of the board(Row)
# Example: if Y = 1 then board[y] = the second row
# X is the width of the board
# Example if X = 1 then board[1][x] is the second element of the second row
# len(board[1]) will be the maximum X value
# D is the direction(Ex: Right , Down)
# B is the board(Ex: board1 , board2)
# Sign is the sign that takes place on the board instead of "-"
# The sign will be different for each player

def make_ship(y, x, d, b, sign):
    count = 0
    if d == "right":
        while (y + count) < len(b[1]) and count <= 3:
            b[y][(x+count)] = sign
            count += 1
    if d == "down":
        while (ship_y + count) < len(b) and count <= 3:
            b[y+count][(x)] = sign
            count += 1


def main():
    global direction, ship_y, ship_x

# 1.The random function will choose who will start

    choose_starting_player()

# 2.Now we print the startin player

    print_starting_player()

# 3.Now we will ask the player one to choose his ship position

    direction = set_direction()
    ship_y = set_position_y() - 1
    ship_x = set_position_x() - 1

# 5.Now we make the first player's ship

    make_ship(ship_y, ship_x, direction, board1, "S")

# 6.Now we print the first player board

    print_board(board1)

# 7.Now we clear the first player's board

    # clear()

# A.We ask the second player to choose his ship position

    direction = set_direction()
    ship_y = set_position_y() - 1
    ship_x = set_position_x() - 1

# B.Now we make the second player's ship

    make_ship(ship_y, ship_x, direction, board2, "L")

# B.We print the second player's board
    print_board(board2)


main()
