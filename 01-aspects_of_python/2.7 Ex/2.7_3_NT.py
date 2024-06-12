# 3 by 22208430

def rotateL(lst_input):
    if len(lst_input) == 0:
        return 'The list/string is empty'
    return lst_input[1:len(lst_input)] + lst_input[:1]

print(rotateL([1, 2, 3, 4, 6, 7]))
print(rotateL('1234567'))

def rotateR(str_input):
    if len(str_input) == 0:
        return 'The list/string is empty'
    return f'{ str_input[-1:len(str_input)] + str_input[0:-1]}'

print(rotateR('Thor'))
print(rotateR([1, 2, 3, 4, 6, 7]))
