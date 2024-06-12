# 5 by 22208430

def rotateRx(lst_input):
    if len(lst_input) <= 1:
        return 'The string is empty'

    last_elem = lst_input[-1]
    lst_input[1:] = lst_input[:-1]
    lst_input[0] = last_elem


l = '1234'
print(rotateRx(list(l)))