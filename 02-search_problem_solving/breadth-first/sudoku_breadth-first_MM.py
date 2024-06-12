# 22200849, 22207839, 22208430

import copy

from breadth_first_algo import BreadthFirstSearch


def isGoal(s):
    for row in s:
        if 0 in row:
            return False
    return True


def find_empty_cell(s):
    for row in range(len(s)):
        for col in range(len(s[row])):
            if s[row][col] == 0:
                return row, col


def nextStates(s):
    i, j = find_empty_cell(s)
    return [fill(s, i, j, n) for n in range(1, 10) if allowed(s, i, j, n)]


def fill(s, i, j, n):
    new_s = copy.deepcopy(s)
    new_s[i][j] = n
    return new_s


def check_line(s, row, n):
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
    if check_line(s, i, n):
        return False
    elif check_line(transpose(s), j, n):
        return False
    elif check_box(s, i, j, n):
        return False
    else:
        return True


def transpose(matrix):
    transposed_matrix = [[row[i] for row in matrix]
                         for i in range(len(matrix[0]))]
    return transposed_matrix


def print_sudoku(grid):
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
# answer differs in one of the rows with DFS (but works slower):
result = BreadthFirstSearch(grid, isGoal, nextStates)
"""
sudoku_breadth-first_MM.py"
5 3 4 | 6 7 8 | 1 9 2 
6 7 2 | 1 9 5 | 3 4 8 
1 9 8 | 3 4 2 | 5 6 7 
---------------------
8 5 9 | 7 6 1 | 4 2 3 
4 2 6 | 8 5 3 | 9 7 1 
7 1 3 | 9 2 4 | 8 5 6 
---------------------
9 6 1 | 5 3 7 | 2 8 4 
2 8 7 | 4 1 9 | 6 3 5 
3 4 5 | 2 8 6 | 7 1 9 

sudoku_depth-first_MM.py"
5 3 4 | 6 7 8 | 9 1 2 
6 7 2 | 1 9 5 | 3 4 8 
1 9 8 | 3 4 2 | 5 6 7 
---------------------
8 5 9 | 7 6 1 | 4 2 3 
4 2 6 | 8 5 3 | 7 9 1 
7 1 3 | 9 2 4 | 8 5 6 
---------------------
9 6 1 | 5 3 7 | 2 8 4 
2 8 7 | 4 1 9 | 6 3 5 
3 4 5 | 2 8 6 | 1 7 9 

"""

print_sudoku(result[-1])  # we are only interested in result and not in path
