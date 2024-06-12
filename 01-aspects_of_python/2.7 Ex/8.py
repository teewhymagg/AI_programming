# 22211514

# the lists in python are mutable, so that is why I created l with two similar sublist.
# If you refer one of them the second will be also affected.
sub_list = [1, 2, 3]

# defining the list which is provided in the task
l = [sub_list, sub_list]

print(l)

# function which pops the last element of the list and inserts it to the beginning


def rotateRx(list):
    list.insert(0, list.pop())


rotateRx(l[0])

print(l)
