import os


class DivisionError(Exception):
    pass


with open(os.path.abspath('numbers.txt'), encoding='UTF-8', mode='r') as file:
    for i in file:
        a, b = map(int, i.split())
        if a < b:
            raise DivisionError('First number smaller than second number!')
        else:
            print(a / b)
