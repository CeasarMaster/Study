from typing import Callable

counter= 0


def count(func: Callable):
    def wrapped_fun(*args, **kwargs):
        global counter
        value = func(*args, **kwargs)
        counter += 1
        print(counter)
        return value

    return wrapped_fun


@count
def hello():
    print('Hello,world')


hello()
hello()
