from typing import Callable


def bread(func: Callable):
    def wrapped_func(*args, **kwargs):
        print('</------\>')
        value = func(*args, **kwargs)
        print('<\______/>')
        return value

    return wrapped_func


def ingredients(func: Callable):
    def wrapped_func(*args, **kwargs):
        print(f'#tomato#')
        value = func(*args, **kwargs)
        print(f'~salad~')
        return value

    return wrapped_func


@bread
@ingredients
def nachinka():
    print(f'--ham--')


nachinka()
