# square_root = lambda a: a * a
# print(square_root(4))
# print(square_root(5))
import time
from typing import Callable


def timer(func: Callable, *args, **kwargs):
    '''Timer function measures the time of a given function'''
    start = time.time()
    func(*args, **kwargs)
    finish = time.time()
    print(f'Time: {finish - start}')


def cubes():
    n = 1000
    summa = 0
    for i in range(1, 1000):
        summa += sum([j ** 3 for j in range(i)])
    return summa


def cubes_2(num: int, num2: int):
    n = num
    summa = num2
    for i in range(1, n + 1):
        summa += sum([j ** 3 for j in range(i)])
    return summa


print(timer.__doc__)  # documentation
print(cubes)
print(cubes.__name__)
timer(cubes)
timer(cubes_2, int(input('Insert the number: ')), 100)
