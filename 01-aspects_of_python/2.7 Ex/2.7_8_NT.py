# 8 by 22208430

def rotateRx(lst_input):
    if len(lst_input) == 0:
        return 'The list is empty'

    last_elem = lst_input[-1]
    lst_input[1:] = lst_input[:-1]
    lst_input[0] = last_elem

l = [1, 2, 3, 4]
list = [l, l]

rotateRx(list[1])
print(list)
