# class Human:
#
#     def __init__(self, name: str, eyes_colour: str, age: int):
#         self.name = name
#         self.eyes_colour = eyes_colour
#         self.age = age
#         self.children = []
#         self.grades = 0
#
#     def school(self) -> None:
#         print(f'{self.name} is going to school.')
#
#     def grades_change(self, grade):
#         self.grades = grade
#
#
# vasya = Human('vasya', 'brown', 15)
# print(vasya.eyes_colour, vasya.age)
# vasya.school()
# petya = Human('petya', 'blue', 16)
# print(petya.eyes_colour, petya.age)
# petya.school()
# petya.school()
# print(petya.grades)
# petya.grades_change(5)
# print(petya.grades)


class Toyota:

    def __init__(self, colour: str, price: int, speed: int, current_speed: int):
        self.colour = colour
        self.price = price
        self.speed = speed
        self.current_speed = current_speed

    def information(self):
        print(f'{self.colour}\n{self.price}\n{self.speed}\n{self.current_speed}')

    def current_speed_change(self, speed_change):
        self.current_speed = speed_change


car = Toyota('Black', 1000000, 200, 0)
car.information()
car.current_speed_change(125)
print(car.current_speed)


