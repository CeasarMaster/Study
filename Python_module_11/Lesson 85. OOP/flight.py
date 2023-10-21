class CanFly:
    def __init__(self, altitude=0, speed=0):
        self.altitude = altitude
        self.speed = speed

    def __str__(self):
        return f'Altitude: {self.altitude}\nSpeed: {self.speed}'

    def takeoff(self):
        pass

    def fly(self):
        pass

    def land(self):
        self.altitude = 0
        self.speed = 0


class Butterfly(CanFly):
    def takeoff(self):
        self.altitude = 1

    def fly(self):
        self.speed = 0.5


class Rocket(CanFly):
    def takeoff(self):
        self.altitude = 500
        self.speed = 1000

    def land(self):
        self.altitude = 0

    def explode(self):
        print('BOOM!')


rocket = Rocket()
butterfly = Butterfly()

butterfly.takeoff()
butterfly.fly()
rocket.takeoff()
rocket.land()
rocket.explode()
