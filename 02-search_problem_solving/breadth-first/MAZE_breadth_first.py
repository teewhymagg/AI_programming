# 22200849, 22207839, 22211514

from breadth_first_algo import BreadthFirstSearch

maze = [[' ', 'W', ' ', ' ', 'G'],
        [' ', 'W', ' ', 'W', ' '],
        [' ', 'W', ' ', ' ', ' '],
        [' ', ' ', 'W', 'W', ' '],
        [' ', ' ', ' ', ' ', ' ']]

rows = len(maze)
cols = len(maze[0])


directions = {
    'Up': [-1, 0],
    'Down': [1, 0],
    'Left': [0, -1],
    'Right': [0, 1],
}


def isGoal(s):
    i, j = s
    return maze[i][j] == 'G'


def nextStates(s):
    dirs = ['Up', 'Down', 'Left', 'Right']
    return [move(s, d) for d in dirs if allowed(s, d)]


def move(s, d):
    moveI, moveJ = directions[d]
    i, j = s
    return [i + moveI, j + moveJ]


def allowed(s, d):
    moveI, moveJ = directions[d]
    i, j = s
    if i + moveI >= cols or i + moveI < 0:
        return False
    elif j + moveJ >= rows or j + moveJ < 0:
        return False
    elif maze[i + moveI][j + moveJ] == 'W':
        return False
    else:
        return True


print(BreadthFirstSearch([0, 0], isGoal, nextStates))
