# def decorator(func):
#     def wrapped_func(*args, **kwargs):
#         print('Something beautiful 1')
#         value = func(*args, **kwargs)
#         print('Something beautiful 2')
#         return value
#
#     return wrapped_func
#
#
# @decorator
# def area_rectangle(a, b):
#     return a * b
#
#
# print(area_rectangle(5, 7))
# from typing import Callable


# def do_twice(func: Callable)-> Callable:
#     '''Decorator function that calls the main function twice'''
#
#     def wrapped_func(*args, **kwargs)-> tuple:
#         value = func(*args, **kwargs)
#         value2 = func(*args, **kwargs)
#         return value, value2
#
#     return wrapped_func
#
#
# @do_twice
# def greeting(name: str)-> None:
#     '''Function that prints a formatted string'''
#     print('Hello, {name}!'.format(name=name))
#
#
# greeting('Tom')
# print(do_twice.__doc__)
import time
from typing import Callable


def timer(func: Callable):
    def wrapped_func(*args, **kwargs):
        start = time.time()
        value = func(*args, **kwargs)
        finish = time.time()
        print(f'Time: {finish - start}')
        return value

    return wrapped_func


@timer
def cubes():
    n = 1000
    summa = 0
    for i in range(1, 1000):
        summa += sum([j ** 3 for j in range(i)])
    return summa


cubes()
