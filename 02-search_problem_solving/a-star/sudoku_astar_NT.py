# Sudoku by 22208430
grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


def is_goal(current):
    for i in range(9):
        for j in range(9):
            if current[i][j] == 0:
                return False
    return True


def sorting(e):
    return len(e)

# A-star search by 22208430
def AStar(state):
    to_do = [state[:][:]]
    visited = set()
    while to_do:
        to_do.sort(key=lambda current: sorting(current))
        current = to_do.pop()
        if is_goal(current):
            return current
        n = next_states(current)
        for state in n:
            if str(state) not in visited:
                to_do.append(state[:][:])
                visited.add(str(state))

    return 'FAILURE: NO PATH FOUND'


def next_states(c_state):
    i, j = 0, 0
    for rows in range(9):
        for column in range(9):
            if c_state[rows][column] == 0:
                i, j = rows, column

    return [fill(c_state, i, j, digit) for digit in range(1, 10) if allowed(c_state, i, j, digit)]


def fill(state, rows, column, digit):
    new_state = [rows[:] for rows in state]
    new_state[rows][column] = digit
    return new_state


def allowed(state, rows, column, digit):
    for i in range(9):
        if (state[rows][i] == digit) or (state[i][column] == digit):
            return False

    x = (rows // 3) * 3
    y = (column // 3) * 3

    for i in range(x, x + 3):
        for j in range(y, y + 3):
            if state[i][j] == digit:
                return False
    return True


result = AStar(grid)
if result != 'FAILURE: NO PATH FOUND':
    for row in result:
        print(row)
else:
    print(result)
