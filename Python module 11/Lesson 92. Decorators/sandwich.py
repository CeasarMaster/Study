from typing import Callable


def bread(func: Callable):
    def wrapped_func(*args, **kwargs):
        print('</------\>')
        value = func(*args, **kwargs)

        return value

    return wrapped_func


@bread
def sandwich():
    print(f'#tomato#\n\n--ham--\n\n~salad~\n\n\___/')


sandwich()
