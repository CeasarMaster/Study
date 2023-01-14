class Potato:
    def __init__(self, num: int):
        self.num_potato = num
        self.growth_status = ['Sprout', 'Green', 'Ready']
        self.status = self.growth_status[0]

    def __str__(self):
        return f'{self.num_potato}:{self.status}\n'


class Garden:
    def __init__(self, potato_count=4):
        self.potato_list = []
        for i in range(potato_count):
            self.potato_list.append(Potato(i + 1))

    def __str__(self):
        return str([f'{i}' for i in self.potato_list])

    def grow(self):
        for i in self.potato_list:
            i.status = i.growth_status[i.growth_status.index(i.status) + 1]
            print(i.status)


potato = Garden()
print(potato)
potato.grow()
print(potato)
potato.grow()
print(potato)
potato.grow()
print(potato)
potato.grow()
