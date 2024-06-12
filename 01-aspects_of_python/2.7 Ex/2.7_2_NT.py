# 2 by 22208430

def rotateL(lst_input):
    if len(lst_input) == 0:
        return 'The list is empty'

    lst_output = lst_input[1:len(lst_input)]
    lst_output.append(lst_input[0])
    return lst_output


print(rotateL([]))





