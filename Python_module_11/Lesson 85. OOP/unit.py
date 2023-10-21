class Unit:
    def __init__(self, hp=100):
        self.hp = hp

    def get_damage(self, damage=0):
        self.hp -= damage


class Soldier(Unit):

    def get_damage(self, damage):
        self.hp -= damage
        print(f'Health: {self.hp}')


class Person(Unit):

    def get_damage(self, damage):
        self.hp -= damage * 2
        print(f'Health: {self.hp}')


soldier = Soldier()
person = Person()

soldier.get_damage(20)
person.get_damage(20)
