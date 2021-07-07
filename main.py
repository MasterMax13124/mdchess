#!/usr/bin/env python3
from pieceMovements import *

def print_board(board : list):
    for row in board:
        print(" ".join(row))

def parse_input() -> list:
    # to complete, will return coordinates in list, as ["piece name", "row", column"]
    return ["B", 4, 5]

def main():
    board = [
        ["r", "n", "b", "q", "k", "b", "n", "r"],
        ["p" ,"p" ,"p", "p", "p", "p", "p", "p"],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        ["P", "P", "P", ".", "P", "P", "P", "P"],
        ["R", "N", "B", "Q", "K", "B", "N", "R"],
    ]
    print_board(board) 
    """ example:
    if bishopMovements(board, 0) != -1:
        board = replacement(board, "B", bishopMovements(board, 0)[0], bishopMovements(board, 0)[1])
    else:
        print("move isn't legal")
    print_board(board)
    """


if __name__ == '__main__':
    main()
