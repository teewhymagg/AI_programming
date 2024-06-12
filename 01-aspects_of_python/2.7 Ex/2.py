# 22211514

def rotateL(list):
    first_element = list[0]
    rotated_list = list[1:]
    rotated_list.append(first_element)
    return rotated_list


original_list = [1, 2, 3, 4]
rotated_list = rotateL(original_list)

print(original_list)
print(rotated_list)
