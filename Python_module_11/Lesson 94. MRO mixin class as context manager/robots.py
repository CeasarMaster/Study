class Robot:
    def __init__(self, model):
        self.model = model

    def introduce(self):
        print('Im a robot')


class CanFly(Robot):
    def __init__(self, model, altitude=0, speed=0):
        super().__init__(model)
        self.altitude = altitude
        self.speed = speed

    def takeoff(self):
        print(f'Robot {self.model} is taking off...\nAltitude: {self.altitude + 50}\n')

    def fly(self):
        print(f'Robot {self.model} is flying...\nSpeed: {self.speed + 50}\n')

    def land(self):

        print(f'Robot {self.model} is landing...\nSpeed: {self.speed}\nAltitude: {self.altitude}\n')


class SpyDrone(CanFly, Robot):
    def __init__(self, model, altitude=0, speed=0):
        super().__init__(model, altitude, speed)

    def operate(self):
        print(f'Robot {self.model} is looking for targets...\nSpeed: {self.speed + 50}\n')


class BattleDrone(CanFly, Robot):
    def __init__(self, model, altitude=0, speed=0):
        super().__init__(model, altitude, speed)

    def operate(self):
        print(f'Robot {self.model} is defending the military object...\n')


spy_drone = SpyDrone('Spy Drone')
battle_drone = BattleDrone('Battle Drone')

spy_drone.takeoff()
spy_drone.fly()
battle_drone.takeoff()
battle_drone.fly()
spy_drone.operate()
battle_drone.operate()
spy_drone.land()
battle_drone.land()
