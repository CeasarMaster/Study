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
        print(f'Robot {self.model} is taking off...\nAltitude: {self.altitude + 50}')
