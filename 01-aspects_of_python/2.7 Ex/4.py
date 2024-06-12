# 22207839

def rotateRx(my_list):
    if my_list:
        last_element = my_list.pop()  # Remove the last element
        # Insert the last element at the beginning
        my_list.insert(0, last_element)


l = [1, 2, 3, 4]
rotateRx(l)
print(l)  # Output: [4, 1, 2, 3]
