# 22200849, 22207839, 22208430

# set board size
# n = 8

"""
How it works:
1D array [1,2,3,4,5,6,7] represents positions of the queens,
i.e. 1 means queen stays at (0,1), 2 means (1,2) 
(position of element is row, value is col)
"""

def allowed(s, j):
    # 22200849
    """This code checks if queens eat each other on 2D
        board using 1D array using woodoo magic"""
    next_ = len(s)  # position of next queen
    if j in s:  # check array for same row (same col is impossible)
        return False
    for col, row in enumerate(s):  # check diagonal
        if abs(j - row) == abs(next_ - col):
            return False
    return True

# 22208430
def find_state(state, path, todo):
    # 22207839
    sip = state in path  # if same deck was explored
    if sip == True:
        return False
    for p in todo:  # or added to todo
        if state in p:
            return False
    return True


def collect_solutions(n):
    """Function to collect all possible solutions
        several functions are inside in order to pass
        size of board "n" only once
    """
    # 22208430
    def nextStates(s):
        # 22208430
        return [s + [j] for j in range(n) if allowed(s, j)]

    def BreadthFirstSearch(s):  # pseuducode implemented
        # 22200849, 22207839, 22208430
        solutions = []
        toDo = [[s]]
        while len(toDo) != 0:
            path = toDo.pop(0)
            current = path[-1]
            if isGoal(current):
                solutions.append(path[-1])
            for state in nextStates(current):
                if find_state(state, path, toDo):
                    new_path = list(path)
                    new_path.append(state)
                    toDo.append(new_path)
        return solutions

    def isGoal(s):
        # 22200849
        return len(s) == n

    ALL_SOLUTIONS = []  # all solutions
    for i in range(n):
        try:
            solutions = BreadthFirstSearch([i])  # solutions from i-th col
            ALL_SOLUTIONS += solutions
        except Exception:  # was needed fo debug
            pass
    return ALL_SOLUTIONS


def showBoard(solution, show_bare=True):
    """function existing simply to make 
        debugging easier. Only calls display_chessboard"""
    # 22208430
    # decorate display_chessboard
    if show_bare == True:
        print(solution)
    else:
        display_chessboard(solution)


def display_chessboard(arr):
    # 22200849
    # print in readable way
    n = len(arr)

    for row in range(n):
        print("|", end=" ")
        for col in range(n):
            if col == arr[row]:
                print("X |", end=" ")
            else:
                print("  |", end=" ")
        print()
        print("+---" * n + "+")


def solve(n):
    # 22207839
    """search all queense with breadth first and display 1-by-1"""
    solutions = collect_solutions(n)
    print(f'Overall found {len(solutions)} solutions to {n}-queens')
    for solution in solutions:
        showBoard(solution, show_bare=False)
        continue_showing = input("Want more? [Y/n]")
        if continue_showing.lower() == "y" or continue_showing.lower() == "":
            continue
        else:
            break


solve(4)
