#!/usr/bin/env python3

from main import parse_input

def replacement(board, piece, row, column):
    board[parse_input()[1]][parse_input()[2]] = f"{piece}"
    board[row][column] = '.'
    return board

def template(board, piece, moves, player):
    # player : 0 = white, 1 = black
    # return : -1 = move ain't possible, tuple (coordinates) = ain't no problemo bro
    for move in moves:
        row = parse_input()[1] 
        column = parse_input()[2]
        # verifying that the goal square is free
        if (board[row][column] in "PRNBQK" and player == 0 ) or (board[row][column] in "prnbqk" and player == 1):
            return -1
        while (0 <= row + move[0] <= 7 ) and (0 <= column + move[1] <= 7):
            row += move[0]
            column += move[1]
            #print(row, column)
            if board[row][column] == '.':
                continue
            elif (board[row][column] == f"{piece}" and player == 0) or (board[row][column] == f"{piece}".lower() and player == 1):
                # piece found
                return (row,column)
            else:
                # piece meet anything else
                break
    # in case in we didn't find any path :(
    return -1

def bishopMovements(board, player):
    moves = [
        [1,1],
        [-1,-1],
        [-1,1],
        [1,-1]
    ]
    return template(board, "B", moves, player)

def rookMovements(board, player):
    moves = [
        [1,0],
        [-1,0],
        [0,1],
        [0,-1],
    ]
    return template(board, "R", moves, player)

def queenMovements(board, player):
    moves = [
        # basically rook + bishop
        [1,0],
        [-1,0],
        [0,1],
        [0,-1],
        [1,1],
        [-1,-1],
        [-1,1],
        [1,-1]
    ]
    return template(board, "Q", moves, player)

def knightMovements(board, player):
    moves = [
        [2,1],
        [2,-1],
        [-2,1],
        [-2, -1],
        [1, 2],
        [1, -2],
        [-1, 2],
        [-1, -2],
    ]
    if (board[parse_input()[1]][parse_input()[2]] in "PRNBQK" and player == 0) or (board[parse_input()[1]][parse_input()[2]] in "prnbqk" and player == 1):
        return -1
    for move in moves:
        row = parse_input()[1] + move[0]
        column = parse_input()[2] + move[1]
        if (board[row][column] == 'N' and player == 0) or (board[row][column] == 'n' and player == 1):
            return (row,column)
    return -1


