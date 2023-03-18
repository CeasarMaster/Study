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
    sum_num = 0
    with open(os.path.abspath('numbers.txt'), encoding='UTF-8', mode='r') as file:
        lines = file.readlines()
        for i in lines:
            if i != '\n':
                sum_num += int(i)

    print(sum_num)


sum_gen()
