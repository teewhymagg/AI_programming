# [Author: 22211514]

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


print(fib(2))

# The function could be more efficient if the memorizing is implemented.
# So, if we take not 6 but 100(for example) instead, the program will recursively calculate all previous numbers untill 100.
# So, it requires a lot of work. If we could memorize the answers somewhere then take its value to calculate bigger numbers, it will work more effective.
