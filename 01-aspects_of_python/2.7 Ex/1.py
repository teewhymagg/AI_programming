# Nichita Trofanisin 22208430
def rotateR(str_input):
    str_output = ''
    if len(str_input) == 0:
        return str_output
    str_output = str_input[-1] + str_input[0:-1]
    return str_output

print(rotateR('Thor'))
