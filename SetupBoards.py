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
    board1.append(["-"] * 8)

for columns in range(8):
    board2.append(["-"] * 8)


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


# This script ask the player
# To choose where he wants to position his ship


def set_position_y():
    correct_value = True
    while correct_value is True:
        try:
            ship_y = int(input("Choose a row: "))
            assert ship_y > 0 and ship_y < 9
            correct_value = False
        except (AssertionError, ValueError):
            print("Please insert a number between 1 and 8")   
    return ship_y-1


def set_position_x():
    correct_value = True
    while correct_value is True:
        try:
            ship_x = int(input("Choose a column: "))
            assert ship_x > 0 and ship_x < 9
            correct_value = False
        except (AssertionError, ValueError):
            print("Please insert a number between 1 and 8")  
    return ship_x-1


correct_direction_values=["right", "down", "DOWN","RIGHT","Right","Down","R","D","d","R","r"]

def set_direction():
    correct_value = True
    while correct_value is True:
        try:
            direction = input("Choose a direction(down or right): ")
            if direction not in correct_direction_values :
                raise Exception
            else:
                correct_value = False
        except (ValueError,Exception):
            print("Please choose between right or down")
    return direction



ship_y = set_position_y()
ship_x = set_position_x()
direction = set_direction()

right_direction = True
down_direction = True

while right_direction == True:
    try:
        assert ship_x < 5
        right_direction = False
        
    except AssertionError:
        print("Nu incape")
        right_direction = True
        ship_x = set_position_x()

while down_direction == True:
    try:
        assert ship_y < 5
        down_direction = False
        
    except AssertionError:
        print("Nu incape")
        down_direction = True
        ship_y = set_position_y()

# def fit_in_board(is_direction, coord, set_position):
#     while is_direction is True:
#         try:
#             assert coord < 5
#             is_direction = False

#         except AssertionError:
#             print("Nu incape")
#             is_direction = True
#             coord = set_position

# fit_in_board(down_direction,ship_y,set_position_y())
# fit_in_board(right_direction,ship_x,set_position_x())
        




# This script will put the ship on the board

print(len(board1))
def make_ship(y,x,d,b):
    global ship_y, ship_x, direction
    count=0
    if b == board1:
        if d == "right":
            while (ship_x + count) < len(b[1]) and count <= 3:
                b[ship_y][(ship_x+count)] = "S"
                count += 1
        if d == "down":
            while (ship_y + count) < len(b) and count <= 3:
                b[ship_y+count][(ship_x)] = "S"
                count += 1
                
    elif b == board2:
        b[ship_y[c]][ship_x[c]] = "1"
       

make_ship(ship_y,ship_x,direction,board1)
print_board(board1)
