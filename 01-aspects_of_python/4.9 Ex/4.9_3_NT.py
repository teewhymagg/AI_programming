# 3 by 22208430
def nsp(x, y):
    
    if x == 0 or y == 0:
        return 1

    return nsp(x - 1, y) + nsp(x, y - 1)

print(nsp(2, 3))
