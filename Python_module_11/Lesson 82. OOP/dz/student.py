class Student:

    def __init__(self, name: str, surname: str, group: int, progress: list):
        self.name = name
        self.surname = surname
        self.group = group
        self.progress = progress
        self.average_rating = sum(self.progress) / len(self.progress)

    def __str__(self):
        return f'Name: {self.name}\nSurname: {self.surname}\nGroup: {self.group}\nProgress: {self.progress}'

    def average(self):
        return self.average_rating


students = [
    Student('Nikita', 'Dereza', 3, [3, 4, 3, 5]),
    Student('Nikita', 'Dereza', 3, [5, 5, 5, 5]),
    Student('Nikita', 'Dereza', 3, [4, 4, 4, 4]),
    Student('Nikita', 'Dereza', 3, [3, 3, 3, 3]),
    Student('Nikita', 'Dereza', 3, [4, 3, 2, 5]),
    Student('Nikita', 'Dereza', 3, [2, 2, 2, 2]),

]
students = sorted(students, key=lambda a: a.average())
for i in students:
    print(i)
