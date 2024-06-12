# 22200836

def nsp(x, y):
    def count_paths(i, j):
        if i == 0 and j == x:
            return 1
        # Initialize paths to 0
        paths = 0
        if i > 0:  
            paths += count_paths(i - 1, j)
        if j < x:  
            paths += count_paths(i, j + 1)
        return paths
    return count_paths(y, 0)

# Example usage
result = nsp(3, 2)
print(result)
