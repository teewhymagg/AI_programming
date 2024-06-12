# [Author: 22207839]

# Initialize function that gets 2 parametrs x and y
def number_paths(x, y):
    # Initialize function that checks if the move is valid by making sure
    # that i = x and j = y are between given coordinates and position is 
    # not visited still
    def is_valid_move(i, j):
        return 0 <= i <= y and 0 <= j <= x and not visited[i][j]

    # algorythm of backtrack that gets i, j and path 
    def backtrack(i, j, path):
        nonlocal count, paths
        # if it is the up-right corner than path is appended and counted
        if i == 0 and j == x:
            count += 1
            paths.append(path)
            return

        # Changing cells in matrix to True when i and j coordinates are visited
        visited[i][j] = True

        # Explore valid moves (up, down, left, right)
        moves = [(i-1, j, 'U'), (i+1, j, 'D'), (i, j-1, 'L'), (i, j+1, 'R')]
        for ni, nj, move in moves:
            if is_valid_move(ni, nj):
                backtrack(ni, nj, path + move)

        visited[i][j] = False  # Backtrack

    count = 0
    paths = []
    # Initialize visited 2d matrix so it can be fullfilled with True or False  
    visited = [[False for _ in range(x+1)] for _ in range(y+1)]

    # Start the backtracking from the bottom-left corner
    backtrack(y, 0, "")

    print("Total paths:", count)
    for path in paths:
        visualize_path(x, y, path)
        print(path)

def visualize_path(x, y, path):
    grid = [['.' for _ in range(x+1)] for _ in range(y+1)]
    grid[0][x] = 'E' # E is End
    i, j = y, 0
    step = 0
    for move in path:
        if move == 'U':
            grid[i][j] = '^'
            i -= 1
        elif move == 'D':
            grid[i][j] = 'v'
            i += 1
        elif move == 'L':
            grid[i][j] = '<'
            j -= 1
        elif move == 'R':
            grid[i][j] = '>'
            j += 1
        step += 1

    # Print grids with moves so it can be easily observed
    print("_" * ((x+1) * 2 + 1))
    for row in grid:
        print("|"+"|".join(row)+"|")
    print("‾" * ((x+1) * 2 + 1))

# Call fuction with 3 (=4) points on x axis and 2 (=3) on y axis
number_paths(3, 2)
