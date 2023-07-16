# List rearranging to add new element algorithm:

lst = []
index = int(input('Insert the index: '))
lst.append(None)
while index > 0 and lst[index - 1] is None:
    lst[index] = lst[index - 1]
    index -= 1
