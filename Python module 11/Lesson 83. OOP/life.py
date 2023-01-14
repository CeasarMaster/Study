import random


class House:

    def __init__(self, money=0, fridge=50):
        self.money = money
        self.food = fridge


house = House()


class Human:

    def __init__(self, name: str, house: bool, satiety=50):
        self.name = name
        self.house = house
        self.satiety = satiety

    def eat(self):
        # +satiety, -food
        self.satiety += 10
        house.food -= 10
        print('Human is eating...')
        print(f'Satiety: {self.satiety}')
        print(f'Food left in the fridge: {house.food}')

    def work(self):
        # -satiety, +money
        self.satiety -= 10
        house.money += 20
        print('Human is working...')
        print(f'Satiety: {self.satiety}')
        print(f'Money: {house.money}')

    def play(self):
        # -satiety
        self.satiety -= 10
        print('Human is playing...')
        print(f'Satiety: {self.satiety}')

    def shop(self):
        # +food, -money
        house.food += 10
        house.money -= 10
        print('Human is shopping...')
        print(f'Food left in fridge: {house.food} ')
        print(f'Money: {house.money}')


human1 = Human('Nikita', True)

rand_num = random.randint(1, 6)
for day in range(1, 365 + 1):
    print(f'\nDay {day}:\n')
    if human1.satiety < 20:
        human1.eat()

    elif human1.satiety <= 0:
        print('Human is dead')
        break

    elif house.food < 10:
        human1.shop()

    elif house.money < 50:
        human1.work()

    elif rand_num == 1:
        human1.work()

    elif rand_num == 2:
        human1.eat()

    else:
        human1.play()
