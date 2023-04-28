class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f'Name: {self.name}\nAge: {self.age}\nGender: {self.gender}')

    def think(self):
        print(f'{self.name} is thinking...')


class Parent(Human):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def introduce(self):
        print(f'Parent Name: {self.name}\nParent Age: {self.age}\nParent Gender: {self.gender}')

    def care(self):
        print(f'Parent {self.name} is taking care of the child...')


class Worker(Human):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    # def introduce(self):
    #     print(f'Worker Name: {self.name}\nWorker Age: {self.age}\nWorker Gender: {self.gender}')

    def work(self):
        print(f'Worker {self.name} is working...')


class Citizen(Worker, Parent):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    # def introduce(self):
    #     print(f'Citizen Name: {self.name}\nCitizen Age: {self.age}\nCitizen Gender: {self.gender}')

    def pay_taxes(self):
        print(f'Citizen {self.name} pays the taxes...')
