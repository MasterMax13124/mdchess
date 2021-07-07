#!/usr/bin/env python3
from pieceMovements import *

def printBoard(board : list):
    for row in board:
        print(" ".join(row))
    print()

def parse_input(move_input : str) -> list:
    # to complete, will return coordinates in list, as ["piece name", "row", column"]
    return ["B", 4, 5]


def main():
    board = [
        ["r", "n", "b", "q", "k", "b", "n", "r"],
        ["p" ,"p" ,"p", "p", "p", "p", "p", "p"],
        ["."]*8,
        ["."]*8,
        ["."]*8,
        ["."]*8,
        ["P", "P", "P", ".", "P", "P", "P", "P"],
        ["R", "N", "B", "Q", "K", "B", "N", "R"],
    ]
    printBoard(board) 

    #example:
    player = 0
    player_move = parse_input("") #will later contain input()
    old_position = bishopMovements(board, player, player_move)
    print("Old position: " + ''.join(str(old_position)))
    print("New position: " + str(player_move[1]) + "," + str(player_move[2]))
    if old_position != -1:
        board = replacement(board, player_move, old_position)
        pass
    else:
        print("Illegal move")
    #end of example

    printBoard(board)


if __name__ == '__main__':
    main()
