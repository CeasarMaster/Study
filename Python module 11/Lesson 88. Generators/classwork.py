# # def square_gen():
# #     for i in range(1, n):
# #         yield i ** 2
# #
# #
# # n = int(input('Insert the number: '))
# #
# # for i in square_gen():
# #     print(i)
#
# n = int(input('Insert the number: '))
# x = (i ** 2 for i in range(1, n))
# for i in x:
#     print(i)

import os


def sum_gen():
    with open(os.path.abspath('numbers.txt'), encoding='UTF-8', mode='r') as file:
        lines = file.readlines()
        for i in lines:
            yield i


sum_num = 0
gen = sum_gen()
for i in gen:
    for j in i.split():
        sum_num += int(j)
print(sum_num)
sum_num = 0
for i in gen:
    for j in i.split():
        sum_num += int(j)
print(sum_num)
