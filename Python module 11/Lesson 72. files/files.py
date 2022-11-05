# import os
#
# with open(os.path.abspath('text.txt'), encoding='UTF-8', mode='r') as file:
#     # n=file.read(10)
#     # print([n])
#     # print(file.readlines())
#     for i_line in file:
#         print(i_line)

import os

# with open(os.path.abspath('text.txt'),encoding='UTF-8',mode='r') as file,open(os.path.abspath('text2.txt'),encoding='UTF-8',mode='w') as file2:
#     n=file.read()
#     file2.write(n)

with open(os.path.abspath('numbers.txt'), encoding='UTF-8', mode='r') as file, open(os.path.abspath('sum_numbers.txt'),
                                                                                    encoding='UTF-8',
                                                                                   mode='w') as file2:
    sum_num = 0
    for i in file:
        sum_num+=int(i)
    file2.write(f'Sum of the numbers: {str(sum_num)}')

