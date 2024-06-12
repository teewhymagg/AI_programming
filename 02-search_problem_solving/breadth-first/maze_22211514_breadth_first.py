# [Author: 22211514]

from collections import deque

# example maze represented as a 2D grid
maze = [
    ['S', ' ', ' ', ' ', ' ', ' '],
    ['W', ' ', 'W', ' ', 'W', ' '],
    ['W', ' ', ' ', ' ', ' ', ' '],
    [' ', 'W', ' ', 'W', 'W', ' '],
    ['W', ' ', 'F', ' ', ' ', ' ']
]

# define the directions
dirs = [(0, 1),
        (0, -1),
        (1, 0),
        (-1, 0)]

# check if the move is within the bounds of the maze and not a wall


def is_valid_move(maze, x, y):
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != 'W'


def isGoal(s, maze):
    i, j = s
    return maze[i][j] == 'F'  # finish

#


def nextStates(s, maze):
    i, j = s
    next_states = []

    for dx, dy in dirs:
        new_i, new_j = i + dx, j + dy

        if is_valid_move(maze, new_i, new_j):
            next_states.append((new_i, new_j))

    return next_states

# breadth first search implementation


def breadth_first_search(maze, initial_state):
    to_do = deque([[initial_state]])

    while to_do:
        path = to_do.popleft()
        current = path[-1]

        if isGoal(current, maze):
            return path

        for state in nextStates(current, maze):
            if state not in path and not any(state in p for p in to_do):
                new_path = list(path)
                new_path.append(state)
                to_do.append(new_path)

    return "FAILURE: NO PATH FOUND"


initial_state = (0, 0)  # starting position
result = breadth_first_search(maze, initial_state)

if result == "FAILURE: NO PATH FOUND":
    print(result)
else:
    print("Path found:", result)
