#!/usr/bin/env python3

from main import parse_input

def replacement(board, player_move, old_position):
    board[player_move[1]][player_move[2]] = f"{player_move[0]}"
    board[old_position[0]][old_position[1]] = '.'
    return board

def template(board, piece, o_row, o_column, moves, player):
    # player : 0 = white, 1 = black
    # return : -1 = move ain't possible, tuple (coordinates) = ain't no problemo bro

    for move in moves:
        # doing this since we cant get static output from parse_input()
        row = o_row 
        column = o_column

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
                return (row,column) #returns the original position of the piece
            else:
                # piece meet anything else
                break
    # in case in we didn't find any path :(
    return -1

# Don't know yet how to limit movement of pawn and king to only one field at a time,
# and allow for diagonal capturing with pawns
# also castling and en passant will need some special exceptions to accomodate
def movements(board, player, player_move):
    movdict = {
        "q" : [
        [1,0],
        [-1,0],
        [0,1],
        [0,-1],
        [1,1],
        [-1,-1],
        [-1,1],
        [1,-1]
        ],
        "b" : [
        [1,1],
        [-1,-1],
        [-1,1],
        [1,-1]
        ],
        "n" : [
        [2,1],
        [2,-1],
        [-2,1],
        [-2, -1],
        [1, 2],
        [1, -2],
        [-1, 2],
        [-1, -2],
        ],
        "r" : [
        [1,0],
        [-1,0],
        [0,1],
        [0,-1],
        ],
        "p" : [
        [1,0]
        ],
        "k" : [
        [1,0],
        [-1,0],
        [0,1],
        [0,-1],
        ]
    }

    moves = movdict[player_move[0].lower()]
    return template(board, player_move[0], player_move[1], player_move[2], moves, player)
