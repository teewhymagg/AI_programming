# 22200836

# Functions in 1st and 2nd exercises do not work both for lists and strings
# If statements to check whether input is list or string can be added

def rotateR(input):
    output = ''

    if len(input) == 0:
        return output

    # if input is string
    if isinstance(input, str):
        output = input[-1] + input[0:-1]
    # if input is list
    elif isinstance(input, list):
        output = [input[-1]] + input[0:-1]

    return output


# Testing with a string
str_input = 'Thor'
print(rotateR(str_input))

# Testing with a list
list_input = [1, 2, 3, 4]
print(rotateR(list_input))

# 2nd exercise can be done by adding if statements to check input type as well


def rotateL(input_L):
    if not input_L:
        return input_L

    if isinstance(input_L, str):
        first_element = input_L[0]
        rotated_input = input_L[1:] + first_element
    elif isinstance(input_L, list):
        first_element = input_L[0]
        rotated_input = input_L[1:] + [first_element]

    return rotated_input


# Testing with a list
original_list = [1, 2, 3, 4]
rotated_list = rotateL(original_list)

print(original_list)
print(rotated_list)

# Testing with a string
original_str = 'Hello'
rotated_str = rotateL(original_str)

print(original_str)
print(rotated_str)
