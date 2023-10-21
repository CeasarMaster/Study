import random


class Battle:
    def __init__(self, hp: int):
        self.fighter_1 = hp
        self.fighter_2 = hp

    def fight(self, damage=20):

        while True:
            index = random.randint(0, 2)
            if index == 0:
                self.fighter_2 -= damage
                print(f'Fighter 1 has attacked Fighter 2. Fighter 2 hp: {self.fighter_2}')
            else:
                self.fighter_1 -= damage
                print(f'Fighter 2 has attacked Fighter 1. Fighter 1 hp: {self.fighter_1}')

            if self.fighter_1 == 0:
                print(f'Fighter 2 won the battle!')
                break
            if self.fighter_2 == 0:
                print('Fighter 1 won the battle!')
                break


fighter = Battle(100)
fighter.fight()
