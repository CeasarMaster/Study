class Unit:
    def __init__(self, hp=0):
        self.hp = hp

    def get_damage(self):
        return self.hp


class Soldier(Unit):

    def get_damage(self):
        print(f'Damage taken: {self.hp}')


class Person(Unit):

    def get_damage(self):
        print(f'Damage taken: {self.hp * 2}')


soldier = Soldier(20)
person = Person(20)

soldier.get_damage()
person.get_damage()
