class Dot:

    def __init__(self, x=0, y=0):
        self.x_cord = x
        self.y_cord = y

    def __str__(self):
        return f'Dot:\n   x coordinate= {self.x_cord}\n   y coordinate= {self.y_cord}'

    def get_x(self):
        return self.x_cord

    def set_x(self):
        if isinstance(self.x_cord, int):
            print('Correct format')

        else:
            print('Incorrect format')

    def get_y(self):
        return self.y_cord

    def set_y(self):
        if isinstance(self.y_cord, int):
            print('Correct format')

        else:
            print('Incorrect format')


dot = Dot()
print(dot)

print(dot.get_x())
dot.set_x()
print(dot.get_y())
dot.set_y()
