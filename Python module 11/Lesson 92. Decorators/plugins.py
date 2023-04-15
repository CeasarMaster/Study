import time
from typing import Callable

plugins = {}


def plugin(func: Callable):
    def wrapped_func(*args, **kwargs):
        value = func(*args, **kwargs)
        plugins['plugin'] = func
        return value

    return wrapped_func


@plugin
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


timer(cubes)
print(plugins)
