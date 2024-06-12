# Authors: 22200836, 22211514, 22208430

# dimension of the puzzle
N = 3

# the goal configuration
goal = [[i * N + j for j in range(N)] for i in range(N)]

# check if the current state is the goal state [Author: 22200836]
def isGoal(s):
    return s == goal

# find the 0 tile in the current state [Author: 22200836]
def find_0(s):
    for i in range(N):
        for j in range(N):
            if s[i][j] == 0:
                return i, j
    return None


# checking the allowed movements [Author: 22200836]
def allowed(s, direction, i, j):
    if direction == "Up" and i > 0:
        return True
    elif direction == "Down" and i < N - 1:
        return True
    elif direction == "Left" and j > 0:
        return True
    elif direction == "Right" and j < N - 1:
        return True
    return False


# implementing the moves in the puzzle [Author: 22200836]
def move(s, direction, i, j):
    s_new = [row[:] for row in s]
    if direction == "Up":
        s_new[i][j], s_new[i - 1][j] = s_new[i - 1][j], s_new[i][j]
    elif direction == "Down":
        s_new[i][j], s_new[i + 1][j] = s_new[i + 1][j], s_new[i][j]
    elif direction == "Left":
        s_new[i][j], s_new[i][j - 1] = s_new[i][j - 1], s_new[i][j]
    elif direction == "Right":
        s_new[i][j], s_new[i][j + 1] = s_new[i][j + 1], s_new[i][j]
    return s_new


# generate the next states from the current state [Author: 22211514]
def nextStates(s):
    i, j = find_0(s)
    dirs = ["Up", "Down", "Left", "Right"]
    return [move(s, d, i, j) for d in dirs if allowed(s, d, i, j)]

def sorting(e):
    return len(e[-1])

# A-star search by 22208430
def a_star(start):
    visited = set()
    queue = [[start, []]]

    while queue:
        queue.sort(key=lambda x: sorting(x), reverse=True)
        state, path = queue.pop()

        visited.add(tuple(tuple(row) for row in state))
        if isGoal(state):
            return path

        for next_state in nextStates(state):
            state_tuple = tuple(tuple(row) for row in next_state)
            if state_tuple not in visited:
                pr_cost = len(path) + 1
                priority = pr_cost + sorting([next_state])
                queue.append([next_state, path + [next_state]])

    return None


# initial state

start = [
    [1,0,2],
    [3,4,5],
    [6,7,8]
]

# function to print the state with step number [Author: 22211514]
def print_state(s, step_number=None):
    if step_number is not None:
        print(f"Step {step_number}:")
    for row in s:
        print(' '.join(map(str, row)))
    print()


# find the solution
solution = a_star(start)

# print the solution path
if solution is not None:
    print("Initial State:")
    print_state(start)
    step_number = 1
    print("Steps to the goal (A*):")
    for step in solution:
        print_state(step, step_number)
        step_number += 1
else:
    print("No solution found.")
