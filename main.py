#!/usr/bin/env python3

def printBoard(board : list):
    for row in board:
        print(" ".join(row))

def parse_input() -> list[str]:
    # to complete, will return coordinates in list, as ["piece name", "row", column"]
    return []


def main():
    board = [
        ["r", "n", "b", "q", "k", "b", "n", "r"],
        ["p" ,"p" ,"p", "p", "p", "p", "p", "p"],
        ["."]*8,
        ["."]*8,
        ["."]*8,
        ["."]*8,
        ["P", "P", "P", "P", "P", "P", "P", "P"],
        ["R", "N", "B", "Q", "K", "B", "N", "R"],
    ]
    printBoard(board) 

if __name__ == '__main__':
    main()
