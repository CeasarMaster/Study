class Boat:

    def __init__(self, cargo='Cargo Ship', cargo_load=0, military='Military Ship'):
        self.cargo_ship = cargo
        self.cargo_load = cargo_load
        self.military_ship = military

    def __str__(self):
        n = input('What ship is sailing?')
        if n == 'cargo'.lower():
            print(f'{self.cargo_ship} is sailing')
            cargo_ship.load()
            cargo_ship.unload()
        elif n == 'military'.lower():
            print(f'{self.military_ship} is sailing')
            military_ship.attack()

        else:
            return 'Model does not exist...'


class CargoShip(Boat):
    def load(self):
        q = input('Would you like to load the ship?')
        if q == 'yes'.lower():
            for i in range(0, 100, 10):
                self.cargo_load += 10
                print(f'Current load: {self.cargo_load}%')
            print('Cargo Loaded!')

    def unload(self):
        q = input('Would you like to unload the ship?')
        if q == 'yes'.lower():
            for i in range(100, 0, -10):
                self.cargo_load -= 10
                print(f'Current load: {self.cargo_load}%')
            print('Cargo Unloaded!')


class MilitaryShip(Boat):
    def attack(self):
        q = input('Would you like to attack?')
        if q == 'yes'.lower():
            print('Military Ship is now attacking...')
        else:
            print('Military Ship will not attack...')


boat = Boat()
cargo_ship = CargoShip() 
military_ship = MilitaryShip()
print(boat)
