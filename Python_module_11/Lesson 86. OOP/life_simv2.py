import os
import random
from random import choice


class Programmer:
    def __init__(self, karma=0):
        self.karma = karma

    def get_karma(self):
        return self.karma

    def set_karma(self, enlightenment):
        self.karma += enlightenment


class KillError(Exception):
    def __str__(self):
        return 'KillError'


class DrunkError(Exception):
    def __str__(self):
        return 'DrunkError'


class CarCrashError(Exception):
    def __str__(self):
        return 'CarCrashError'


class GluttonyError(Exception):
    def __str__(self):
        return 'GluttonyError'


class DepressionError(Exception):
    def __str__(self):
        return 'DepressionError'


programmer = Programmer()
reasons = [
    KillError(),
    DrunkError(),
    CarCrashError(),
    GluttonyError(),
    DepressionError()
]


def one_day(file):
    try:
        if random.randint(1, 10) == 1:
            raise choice(reasons)


    except Exception as error:
        file.write(f'{error}\n')

    return random.randint(1, 7)


with open(os.path.abspath('karma.log'), encoding='UTF-8', mode='w') as karma_log:
    while programmer.get_karma() < 500:
        programmer.set_karma(one_day(karma_log))
print('Enlightenment achieved')
