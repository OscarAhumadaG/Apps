from random import randrange

import numpy as np


def ShowBoard(board,n):
    print("+-------"*n,"+", sep="")
    for row in range(n):
        print("|       "*n,"|", sep="")
        for col in range(n):
            if len(str(board[row][col]))==1:
                print("|   ",str(board[row][col]),"   ",sep='',end="")
            elif len(str(board[row][col]))==2:
                print("|   ", str(board[row][col]), "  ", sep='', end="")
        print("|")
        print("|       " * n, "|", sep="")
        print("+-------" * n, "+", sep="")


def UserMovement(board,sign):
    size = len(board)
    check = True
    while check:
        move = input("Please enter your move: ")
        check = (len(move) > len(f"{size*size}"))  or (move < "1") or (int(move) > size*size)

        if check:
            print("Bad movement - please repeat your input")
            continue
        move = int(move) - 1
        row = move // len(board)
        col = move % len(board)
        cell = board[row][col]
        check = cell in ['X','O']
        if check:
            print("Cell is occupied, you need repeat your move")
            continue
        board[row][col] = sign

def CheckFreeCells(board,size):
    FreeCells = []
    for row in range(size):
        for col in range(size):
            if board[row][col] not in ["X","O"]:
                FreeCells.append((row,col))
    return FreeCells


def MachineMove(board, machinesign, size):
    free = CheckFreeCells(board, size)
    cant_cells_free = len(free)
    if cant_cells_free > 0:
        select = randrange(cant_cells_free)
        row,col = free[select]
        board[row][col] = machinesign

def CheckWinner(board, size):
    board = np.array([[1 if cell == "X" else -1 if cell == "O" else 0 for cell in row] for row in board])

    winner = None
    for i in range(size):
        if np.all(board[i, :] == 1) or np.all(board[:, i] == 1):
            winner = 'X'
            return winner
        elif np.all(board[i, :] == -1) or np.all(board[:, i] == -1):
            winner = 'O'
            return winner

    if np.all(np.diag(board) == 1) or np.all(np.diag(np.fliplr(board)) == 1):
        winner = 'X'
        return winner
    elif np.all(np.diag(board) == -1) or np.all(np.diag(np.fliplr(board)) == -1):
        winner = 'O'
        return winner

    return winner

quantity = int(input('Select the dimention that you want: '))

sign_Selection = input("Select the sign that you want to use X or O: ").upper()

if sign_Selection == 'O':
    HumanSign = "O"
    ComputerSign = "X"
else:
    HumanSign = "X"
    ComputerSign = "O"


start_player = input('Select who you want to start Computer (C) or you(M):').upper()

if start_player =="M":
    HumanTurn = True
elif start_player =="C":
    HumanTurn = False

board = [[quantity * j + i + 1 for i in range(quantity)] for j in range(quantity)]
free = CheckFreeCells(board, quantity)
while len(free):

    ShowBoard(board, quantity)
    if HumanTurn:
        UserMovement(board,HumanSign)
        victory = CheckWinner(board,quantity)
    else:
        MachineMove(board,ComputerSign,quantity)
        victory = CheckWinner(board,quantity)

    if victory != None:
        break
    HumanTurn = not HumanTurn
    free = CheckFreeCells(board,quantity)


ShowBoard(board,quantity)
if victory == HumanSign:
	print("You won!")
elif victory == ComputerSign:
	print(" Computer won")
else:
	print("Tie!")


