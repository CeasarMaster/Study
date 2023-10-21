import random


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
