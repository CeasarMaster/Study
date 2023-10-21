import random


class House:

    def __init__(self, money=100, fridge=50, cat_food=30, dirt=0):
        self.money = money
        self.food = fridge
        self.cat_food = cat_food
        self.dirt = dirt

    def __str__(self):
        return f'Money: {self.money}\nFood: {self.food}\nCat Food: {self.cat_food}\nDirt: {self.dirt}'


house = House()


class Human:

    def __init__(self, name: str, satiety=30, happiness=100):
        self.name = name
        self.happiness = happiness
        self.satiety = satiety

    def __str__(self):
        return f'Name: {self.name}\nHappiness: {self.happiness}\nSatiety: {self.satiety}'

    def eat(self):
        # +satiety, -food
        if house.food >=10:
            self.satiety += 10
            house.food -= 10
            print('Human is eating...')
            print(f'Satiety: {self.satiety}')
            print(f'Food left in the fridge: {house.food}')

    def stroke_cat(self):
        print('Cat is being stroked...')
        self.happiness += 5


class Husband(Human):
    def play(self):
        print('Husband is playing...')
        human1.happiness += 20

    def work(self):
        print('Husband is working...')
        house.money += 150


class Wife(Human):
    def shop(self):
        print('The wife is shopping...')
        house.food += 10
        house.cat_food += 10
        house.money -= 20

    def clean_house(self):
        print('Wife is cleaning...')
        house.dirt -= 50

    def buy_shuba(self):
        print('Wife just bought a shuba...')
        house.money -= 350


class Cat:
    def __init__(self, name: str, satiety=30):
        self.name = name
        self.satiety = satiety

    def sleep(self):
        print('Cat is sleeping')

    def cat_eat(self):
        print('Cat is eating')
        self.satiety += 10

    def destroy_wallpaper(self):
        print('The cat is destroying the wallpaper...')
        house.dirt += 5


human1 = Husband('Nikita')
human2 = Wife('X')
cat = Cat('Lucy')

for day in range(1, 365 + 1):
    rand_num = random.randint(1, 6)
    print(f'\nDay {day}:\n')
    house.dirt += 5
    if human1.satiety > 0 and human1.satiety < 20 and house.food >= 10:
        human1.eat()
    elif human2.satiety > 0 and human2.satiety < 20 and house.food >= 10:
        human2.eat()

    elif human1.satiety <= 0:
        print('Husband is dead')
        break
    elif human2.satiety <= 0:
        print('Wife is dead')
        break
    elif cat.satiety <= 0:
        print('Cat is dead...')
        break



    elif house.food < 10:
        human2.shop()

    elif house.money < 50:
        human1.work()

    elif rand_num == 1:
        human1.work()

    elif rand_num == 2 and house.food >= 10:
        human1.eat()
        human2.eat()

    else:
        human1.play()
    print(house, human1, human2, sep='\n\n')
