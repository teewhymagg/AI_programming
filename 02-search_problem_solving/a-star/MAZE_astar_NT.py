# Authors: 22211514, 22208430
maze = [[' ', 'W', ' ', ' ', ' '],
        [' ', 'W', ' ', ' ', 'G'],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', 'W', 'W', ' '],
        [' ', ' ', ' ', ' ', ' ']]

rows = len(maze)
cols = len(maze[0])


def find_state(state, path, todo):
    # 22207839
    """check for state in current path
        and in all ToDo list"""
    sip = state in path
    if sip:
        return False
    for p in todo:
        if state in p:
            return False
    return True

def sorting(e):
    return len(e)

# A-star search by 22208430
def AStar(s):
    toDo = [[s]]
    while toDo:
        toDo.sort(key=lambda x: sorting(x), reverse=False)
        path = toDo[0]
        toDo.pop(0)
        current = path[-1]
        if isGoal(current):
            return path
        for state in nextStates(current):
            if find_state(state, path, toDo):
                new_path = list(path)
                new_path.append(state)
                toDo.append(new_path)
    raise Exception("FAILURE: NO PATH FOUND")


# 22200849
# axis: y down, x right (easier to work with array)
directions = {
    'Up': [-1, 0],
    'Down': [1, 0],
    'Left': [0, -1],
    'Right': [0, 1],
}


def isGoal(s):
    # 22200849
    i, j = s
    return maze[i][j] == 'G'


def nextStates(s):
    # 22207839
    """Access dictionary directions by key and try to
        make a move in maze 
        (by switching by 1/-1 in allowed direction)"""
    dirs = ['Up', 'Down', 'Left', 'Right']
    return [move(s, d) for d in dirs if allowed(s, d)]


def move(s, d):
    # 22207839
    moveI, moveJ = directions[d]
    i, j = s
    return [i + moveI, j + moveJ]


def allowed(s, d):
    # 22200849, 22207839
    """Check all directions and keep in mind array size"""
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


print(AStar([0, 0]))