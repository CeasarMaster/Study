class Person:
    def __init__(self, name: str, surname: str, age: int):
        self.__name = name
        self.__surname = surname
        self.__age = age


class Employee(Person):
    def calc_paycheck(self):
        pass


class Manager(Employee):
    def calc_paycheck(self):
        return 13000


class Agent(Employee):
    def __init__(self, name: str, surname: str, age: int):
        super().__init__(name, surname, age)
        self.earnings = 5000

    def calc_paycheck(self, sales: int):
        return self.earnings + (sales * 0.05)


class Worker(Employee):
    def __init__(self, name: str, surname: str, age: int):
        super().__init__(name, surname, age)
        self.earnings = 100

    def calc_paycheck(self, hours: int):
        return self.earnings * hours


objects = [
    Manager('Nikita', 'Dereza', 15),
    Manager('Sergey', 'Volkov', 15),
    Manager('Maxim', 'Kovalenko', 15),
    Agent('Artem', 'Kovol', 23),
    Agent('Maxim', 'Pechkin', 23),
    Agent('Vasya', 'Ivanov', 23),
    Worker('Petya', 'Vasilyevich', 18),
    Worker('Petya', 'Vasilyevich', 18),
    Worker('Petya', 'Vasilyevich', 18)

]
manager_total = Manager.calc_paycheck(objects[0]) + Manager.calc_paycheck(objects[1]) + Manager.calc_paycheck(
    objects[2])
agent_total = Agent.calc_paycheck(objects[3], 20) + Agent.calc_paycheck(objects[4], 30) + Agent.calc_paycheck(
    objects[5], 40)

worker_total = Worker.calc_paycheck(objects[6], 12) + Worker.calc_paycheck(objects[7], 11) + Worker.calc_paycheck(
    objects[8], 14)

total_pay = manager_total + agent_total + worker_total

print(f'Total paycheck for all employees: {total_pay}')
