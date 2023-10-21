from time import sleep


class Boat:

    def __init__(self, model):
        # self.cargo_ship = cargo
        # self.cargo_load = cargo_load
        # self.military_ship = military
        self.model = model

    def __str__(self):
        return f'Model of Ship: {self.model}'

    def sailing(self):
        print(f'{self.model} is sailing')


class CargoShip(Boat):
    def __init__(self, model, cargo_load=0):
        super().__init__(model)
        self.cargo_load = cargo_load

    def load(self):
        q = input('Would you like to load the ship?')
        if q == 'yes'.lower():
            for i in range(0, 100, 10):
                self.cargo_load += 10
                sleep(1)
                print(f'Current load: {self.cargo_load}%')
            print('Cargo Loaded!')

    def unload(self):
        q = input('Would you like to unload the ship?')
        if q == 'yes'.lower():
            for i in range(100, 0, -10):
                self.cargo_load -= 10
                sleep(1)
                print(f'Current load: {self.cargo_load}%')
            print('Cargo Unloaded!')


class MilitaryShip(Boat):
    def attack(self):
        q = input('Would you like to attack?')
        if q == 'yes'.lower():
            print('Military Ship is now attacking...')
        else:
            print('Military Ship will not attack...')



n = input('What ship is sailing?')
if n == 'cargo'.lower():
    cargo_ship = CargoShip('Cargo')
    print(cargo_ship)
    cargo_ship.load()
    cargo_ship.unload()
elif n == 'military'.lower():
    military_ship = MilitaryShip('Military')
    print(military_ship)
    military_ship.attack()

boat = Boat('Boat')
print(boat)
