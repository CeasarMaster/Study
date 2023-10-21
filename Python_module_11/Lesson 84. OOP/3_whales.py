# INCAPSULATION

# class Student:
#     # static atribute
#     legs = 2
#
#     def __init__(self, name: str, age: int, subjects: dict):
#         self.name = name
#         self.__age = age
#         self.subjects = subjects
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self):
#         self.__age += 1
#
#
# print(Student.legs)
#
# student1 = Student('Nikita', 15, {})
# print(student1.legs)
# student1.set_age()
# print(student1.get_age())


# NASLEDOVANIE
# POLYMORPHISM


class Student:  # SUPER CLASS
    # static atribute
    legs = 2

    def __init__(self, name: str, age: int, subjects: dict):
        self.name = name
        self.__age = age
        self.subjects = subjects

    def go_study(self):
        print(f'{self.name} is going to university')

    def get_age(self):
        return self.__age

    def set_age(self):
        self.__age += 1


class Shkolnik(Student):  # SECONDARY CLASS
    def go_study(self):
        print(f'{self.name} is going to school')


shkolnik = Shkolnik('Nikita', 15, {})
shkolnik.go_study()
