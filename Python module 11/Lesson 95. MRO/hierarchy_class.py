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
        pass


class CanCode(GainExp):
    def __init__(self, exp):
        super().__init__(exp)

    def code(self):
        pass


class CanDrive(Human):

    def __init__(self, name, age, exp):
        super().__init__(name, age, exp)

    def drive(self):
        pass


class Student(Human, Worker):
    def __init__(self, name, age, exp):
        super().__init__(name, age, exp)

    def study(self):
        pass


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
