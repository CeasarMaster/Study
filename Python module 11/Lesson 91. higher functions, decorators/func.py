from typing import Callable


def func_2(func: Callable, *args, **kwargs):
    return func(*args, **kwargs) * func(*args, **kwargs)


def func_1(x):
    return x + 10


print(func_2(func_1, 8))
