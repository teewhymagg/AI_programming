
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
    next_ = len(s)  # position of next queen
    if j in s:  # check array for same row (same col is impossible)
        return False
    for col, row in enumerate(s):  # check diagonal
        if abs(j - row) == abs(next_ - col):
            return False
    return True


def find_state(state, path, todo):
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
    def nextStates(s):
        return [s + [j] for j in range(n) if allowed(s, j)]

    def sorting(e):
        return len(e)

    # A-star search by 22208430
    def AStar(s):
        solutions = []
        toDo = [[s]]
        while len(toDo) != 0:
            toDo.sort(key=lambda x: sorting(x), reverse=False)
            path = toDo[0]
            toDo.pop(0)
            current = path[-1]
            if isGoal(current):
                solutions.append(path[-1])
            for state in nextStates(current):
                if find_state(state, path, toDo):
                    new_path = list(path)
                    new_path.append(state)
                    toDo.append(list(new_path))
        return solutions

    def isGoal(s):
        return len(s) == n

    ALL_SOLUTIONS = []  # all solutions
    for i in range(n):
        try:
            solutions = AStar([i])  # solutions from i-th col
            ALL_SOLUTIONS += solutions
        except Exception:  # was needed fo debug
            pass
    return ALL_SOLUTIONS


def showBoard(solution, show_bare=True):
    # decorate display_chessboard
    if show_bare == True:
        print(solution)
    else:
        display_chessboard(solution)

# 22208430
def display_chessboard(arr):
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
