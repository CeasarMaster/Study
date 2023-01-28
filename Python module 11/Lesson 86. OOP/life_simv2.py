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
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


programmer = Programmer()
kill_error = KillError()
drunk_error = DrunkError()
car_crash = CarCrashError()
gluttony_error = GluttonyError()
depression_error = DepressionError()


def one_day():
    with open(os.path.abspath('karma.log'), encoding='UTF-8', mode='w') as karma_log:
        reason = [kill_error, drunk_error, car_crash, gluttony_error, depression_error]
        try:
            if random.randint(1, 10) == 1:
                raise choice(reason)


        except Exception as error:
            karma_log.write(str(error))

    return random.randint(1, 7)


while programmer.get_karma() > 500:
    programmer.set_karma(one_day())
print('enlightenment achieved')
