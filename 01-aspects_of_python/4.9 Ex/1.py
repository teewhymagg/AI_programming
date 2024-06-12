# Matriculation number: 22208430
def rev(lst):
    if type(lst) == list:
        if len(lst) == 0:
            return []
        else:
            return [lst.pop()] + rev(lst)
    elif type(lst) == str:
        if len(lst) == 0:
            return ''
        else:
            return f'{lst[-1] + rev(lst[0:-1])}'


bruh = list('Programmierung')
print(rev(bruh))
