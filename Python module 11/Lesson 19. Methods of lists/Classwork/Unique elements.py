first_list = [int(input('Insert the 3 numbers of choice:')) for _ in range(3)]
second_list = [int(input('Insert the 7 numbers of choice:')) for _ in range(7)]
first_list.extend(second_list)
for i in first_list:
    while first_list.count(i) > 1:
        first_list.remove(i)
print(first_list)
