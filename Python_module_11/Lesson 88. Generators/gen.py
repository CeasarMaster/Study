# generators
#import time
#
#
# def cube():
#     for i in range(1, 2000):
#         yield i ** 5
#
#
# start = time.time()
#
# for i in cube():
#     print(i)
# finish = time.time()
# print(finish - start)

# generator expressions

import time

start = time.time()
x = (i ** 5 for i in range(1, 2000))
for i in x:
    print(i)

finish = time.time()
print(finish - start)
