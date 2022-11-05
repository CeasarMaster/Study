def open_list(element_list):
    for i in element_list:
        if isinstance(i, int):
            new_list.append(i)
        if isinstance(i, list):
            open_list(i)


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]
new_list = list()
open_list(nice_list)
print(new_list)