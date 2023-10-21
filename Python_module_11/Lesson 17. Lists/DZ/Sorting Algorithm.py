nums_list = []
n = int(input('Insert the number of symbols in the list: '))
for i in range(n):
    x = int(input('Insert the number: '))
    nums_list.append(x)
for i in range(n):
    for j in range(n - i - 1):
        if nums_list[j] > nums_list[j + 1]:
            nums_list[j], nums_list[j + 1] = nums_list[j + 1], nums_list[j]

print('sorted list:', nums_list)
