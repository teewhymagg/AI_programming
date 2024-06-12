# 22200849, 22207839

import copy

from depth_first_algo import DepthFirstSearch


def isGoal(s):
    # 22200849
    for row in s:
        if 0 in row:
            return False
    return True


def find_empty_cell(s):
    # 22207839
    """find first empty cell"""
    for row in range(len(s)):
        for col in range(len(s[row])):
            if s[row][col] == 0:
                return row, col


def nextStates(s):
    # 22200849
    """try to fill next empty cell"""
    i, j = find_empty_cell(s)
    return [fill(s, i, j, n) for n in range(1, 10) if allowed(s, i, j, n)]


def fill(s, i, j, n):
    # 22207839
    new_s = copy.deepcopy(s)
    new_s[i][j] = n
    return new_s


def check_line(s, row, n):
    # 22200849
    """check if we have number in row 
        (will also be used for column via transpose)"""
    if n in s[row]:
        return True
    else:
        return False


def check_box(s, row, col, n):
    row = (row // 3) * 3
    col = (col // 3) * 3
    for i in range(row, row + 3):
        for j in range(col, col + 3):
            if s[i][j] == n:
                return True
    return False


def allowed(s, i, j, n):
    """check if move is allowed based on row/column/box"""
    # 22200849
    if check_line(s, i, n):
        return False
    elif check_line(transpose(s), j, n):
        return False
    elif check_box(s, i, j, n):
        return False
    else:
        return True


def transpose(matrix):
    """needed for transposing and checking existence
        of number in column (numpy had problems)"""
    # 22207839
    transposed_matrix = [[row[i] for row in matrix]
                         for i in range(len(matrix[0]))]
    return transposed_matrix


def print_sudoku(grid):
    """display board in readable way"""
    # 22200849
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(grid[i][j], end=" ")
        print()


grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 0, 0],
]
result = DepthFirstSearch(grid, isGoal, nextStates)
print_sudoku(result[-1])  # we are only interested in result and not in path
