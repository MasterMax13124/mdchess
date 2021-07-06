#!/usr/bin/env python3

def printBoard(board : list):
    for row in board:
        for square in row:
            print(square, end = ' ')
        print()

def parse_input() -> list:
    # to complete, will return coordinates
    pass


def main():
    board = [
        ["r", "n", "b", "q", "k", "b", "n", "r"],
        ["p" ,"p" ,"p", "p", "p", "p", "p", "p"],
        [".", ".",".", ".", ".", ".", ".", "."],
        [".", ".",".", ".", ".", ".", ".", "."],
        [".", ".",".", ".", ".", ".", ".", "."],
        [".", ".",".", ".", ".", ".", ".", "."],
        [".", ".",".", ".", ".", ".", ".", "."],
        ["P", "P", "P", "P", "P", "P", "P", "P"],
        ["R", "N", "B", "Q", "K", "B", "N", "R"],
    ]
    printBoard(board) 

if __name__ == '__main__':
    main()
