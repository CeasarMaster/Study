class Human:

    def __init__(self, name: str, age: int, counter_objects=[]):
        self.__name = name
        self.__age = age

        counter_objects.append(1)
        print(len(counter_objects))

    def check_data(self):
        if not self.__name.isalpha():
            self.__name = input('Insert a new name that contains only letters: ')

        if self.__age not in range(0, 100):
            self.__age = int(input('Value error, insert a new age: '))


human1 = Human('Vasya', 15)
human2 = Human('Petya', 16)
human3 = Human('Liza', 17)

human4 = Human('Ivan', 15)
human5 = Human('Nikita,', 15)

