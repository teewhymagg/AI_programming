# 22200849

"""The program places symbols on the desk in order to determine 
    if it is allowed to place a queen without any sophisticated 
    checks. IE you have 4x4 board and want to place queen  at (1,2)
    [[0 0 0 0]
    [0 0 0 0]
    [0 0 0 0]
    [0 0 0 0]]
    It will look like this 
    [[0 0 0 0]
    [0 0 1 0]
    [0 0 0 0]
    [0 0 0 0]]
    And with constrains for placing objects (not allowed cells):
    [[ 0 -1 -1 -1]
    [-1 -1  1 -1]
    [ 0 -1 -1 -1]
    [-1  0 -1  0]]
    Every queen is 1, not allowed cell is -1, allowed 0
"""

import numpy as np


def print_board(board):
    """display board as intended by task"""
    for row in board:
        for col in row:
            col = "Q" if col == 1 else "."
            print(f'{col}', end="  ")
        print()


def place_constrains(input_board, row, col):
    board = np.copy(input_board)  # just to be safe
    n = len(board)
    board[row] = np.full(n, -1)  # fill rows with -1
    for i in range(-min(row, col), min(n - row, n - col)):
        board[row + i, col + i] = -1  # fill diagonal (parallel to main)

    for i in range(-min(row, n - col - 1), min(n - row, col + 1)):
        board[row + i, col - i] = -1  # fill diagonal (perpendicular to main)

    board[row][col] = 1  # place one at where queen has to be

    tp_board = np.transpose(board)
    tp_board[col] = np.full(n, -1)  # fill cols (in transposed matrix)
    tp_board[col][row] = 1
    board = np.transpose(tp_board)
    return board


def allowed(board, row, col):
    # this check is easy as we do all work in place constrains
    if board[row, col] == 0:
        return True
    else:
        return False


def solve(n):
    # collect all solutions
    board = np.zeros((n, n), dtype=int)
    ALL_SOLUTIONS = []

    def recursive_queens(input_board, row):
        """Do recursive search by cycling every column and
            calling recursion if placement is allowed"""
        board = np.copy(input_board)
        if row == n:
            ALL_SOLUTIONS.append(np.copy(board))
            return
        for col in range(n):
            if allowed(board, row, col):
                recursive_queens(place_constrains(board, row, col), row + 1)

    recursive_queens(board, 0)

    print(f'Overall found {len(ALL_SOLUTIONS)} solutions to {n}-queens')
    for solution in ALL_SOLUTIONS:
        print_board(solution)
        continue_showing = input("Want more? [Y/n/ENTER]")
        if continue_showing.lower() == "y" or continue_showing.lower() == "":
            continue
        else:
            break


solve(5)
