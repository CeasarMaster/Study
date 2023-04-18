# from typing import Callable
#
#
# def how_are_you(func: Callable):
#     def wrapped_func(*args, **kwargs):
#         input('How are you?')
#         print('Im not okay! Here is your function -_-')
#         value = func(*args, **kwargs)
#         return value
#
#     return wrapped_func
#
#
# @how_are_you
# def test():
#     print('Something is happening')
#
#
# test()

# import time
# from typing import Callable
#
#
# def pause(func: Callable):
#     def wrapped_func(*args, **kwargs):
#         time.sleep(2)
#         value = func(*args, **kwargs)
#
#         return value
#
#     return wrapped_func
#
#
# @pause
# def test():
#     for i in range(1, 15):
#         print('Hello, world')
#
#
# test()


import datetime
import os
from typing import Callable


def logging(func: Callable):
    def wrapped_func(*args, **kwargs):

        with open(os.path.abspath('function_errors.log'), encoding='UTF-8', mode='w') as logs:
            errors = []
            try:

                value = func(*args, **kwargs)
                raise ValueError
                print(func, func.__doc__)
            except BaseException as error:
                errors.append(f'{error}')
                logs.write(str(error))

        return value

    return wrapped_func


@logging
def cubes():
    '''functions cubes returns the sum of cubed values'''

    n = 'fdgdghd'
    summa = 0
    for i in range(1, 1000):
        summa += sum([j ** 3 for j in range(i)])
    return summa


cubes()
