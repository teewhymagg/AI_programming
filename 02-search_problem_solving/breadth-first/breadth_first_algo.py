# 22200849

def BreadthFirstSearch(s, isGoal, nextStates):
    toDo = [[s]]
    while len(toDo) != 0:
        path = toDo.pop(0)  # only change from depth_first
        current = path[-1]
        if isGoal(current):
            return path
        for state in nextStates(current):
            if find_state(state, path, toDo):
                new_path = list(path)
                new_path.append(state)
                toDo.append(new_path)


def find_state(state, path, todo):
    sip = state in path
    if sip == True:
        return False
    for p in todo:
        if state in p:
            return False
    return True
