class GainExp:

    def __init__(self, exp=0):
        self.exp = exp

    def show_status(self):
        print(f'Current Experience: {self.exp}')


class Human(GainExp):
    def __init__(self, name, age, exp):
        super().__init__(exp)
        self.name = name
        self.age = age


class Worker(GainExp):
    def __init__(self, exp):
        super().__init__(exp)

    def work(self):
        print('Working...')
        self.exp += 50


class CanCode(GainExp):
    def __init__(self, exp):
        super().__init__(exp)

    def code(self):
        print('Coding...')
        self.exp += 50


class CanDrive(Human):

    def __init__(self, name, age, exp):
        super().__init__(name, age, exp)

    def drive(self):
        print('Driving...')
        self.exp += 50


class Student(Human, Worker):
    def __init__(self, name, age, exp):
        super().__init__(name, age, exp)

    def study(self):
        print(f'Student {self.name} is studying...')
        self.exp += 50


class Male(Human, Worker, CanCode):
    def __init__(self, name, age, exp):
        super().__init__(name, age, exp)


class Programmer(Worker, CanCode):
    def __init__(self, exp):
        super().__init__(exp)


class Biker(CanDrive, Male):

    def __init__(self, name, age, exp):
        super().__init__(name, age, exp)


class Son(Student, Male, Programmer):
    def __init__(self, name, age, exp):
        super().__init__(name, age, exp)


class Nikita(Biker, Son):
    def __init__(self, name, age, exp):
        super().__init__(name, age, exp)
