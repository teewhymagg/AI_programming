# 7 by 22208430

def rotateRx(lst_input):

    if len(lst_input) == 0:
        return 'The list is empty'
    else:
        last_elem = lst_input[-1]
        lst_input[1:] = lst_input[:-1]
        lst_input[0] = last_elem
        last_elem = lst_input[-1]
        lst_input[1:] = lst_input[:-1]
        lst_input[0] = last_elem
        return 'Reversed'


l = [1, 2, 3, 4, 6]
print(rotateRx(l))
print(l)
