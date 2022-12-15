# class Student:
#     def __init__(self, name: str, age: int, city: str, school: int):
#         self.student_name = name
#         self.student_age = age
#         self.city, self.school = city, school
#
#     def __str__(self):
#         return f'Name: {self.student_name}\nAge: {self.student_age}\nCity: {self.city}\nSchool: {self.school}'
#
#
# student = Student('Nikita', 15, 'Moscow', 15)
# print(student)


class Human:

    def __init__(self, name: str, age: int, money: int):
        self.name, self.age, self.money = name, age, money

    def __str__(self):
        return f'Name: {self.name}\nAge: {self.age}\nMoney: {self.money}'

    def lend(self, other, amount):
        if amount > self.money:
            print('Not enough money')
        else:
            other.money += amount
            self.money -= amount


vasya = Human('Vasya', 20, 25000)
petya = Human('Petya', 15, 10000)
print(petya)
print(vasya)
cash = 100000
vasya.lend(petya, cash)
print(petya)
print(vasya)
