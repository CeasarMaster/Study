import math


class Circle:

    def __init__(self, x: int = 0, y: int = 0, radius: int = 1):
        self.x_cord = x
        self.y_cord = y
        self.radius = radius

    def __str__(self):
        return f'x-coordinate = {self.x_cord}\ny-coordinate = {self.y_cord}\nradius = {self.radius}'

    def increase(self):
        question = input('Would you like to increase the size of the circle? ')
        if question == 'yes'.lower():
            r = int(input('Insert the increase size: '))
            self.radius *= r
        else:
            print('No problem!')

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def circles_intersection(self, other_circle):
        a = abs(self.x_cord - other_circle.x_cord)
        b = abs(self.y_cord - other_circle.y_cord)
        sum_radius = self.radius + other_circle.radius
        distance = math.sqrt(a ** 2 + b ** 2)
        if sum_radius < distance:
            return False
        else:
            return True


circle = Circle()
circle_2 = Circle(2, 2, 3)
print(circle)
circle.increase()
print(circle.area())
print(circle.perimeter())
print(circle.circles_intersection(circle_2))

