import time

from typing import Callable


# def func_2(func: Callable, *args, **kwargs):
#     return func(*args, **kwargs) * func(*args, **kwargs)
#
#
# def func_1(x):
#     return x + 10
#
#
# print(func_2(func_1, 8))

def timer(func: Callable, func2: Callable, *args, **kwargs):
    start = time.time()
    func(*args, **kwargs)
    func2(*args, **kwargs)
    finish = time.time()
    print(f'Execution time: {finish - start}')


def flip(num):
    num2 = 0
    while num > 0:
        digit = num % 10
        num = num // 10
        num2 = num2 * 10
        num2 = num2 + digit
    return num2


def sum_flip(num):
    return num + flip(num)


timer(flip, sum_flip, 456575664563452334645656785686798673)
