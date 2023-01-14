class Potato:

    def __init__(self, num: int):
        self.num_potato = num
        self.growth_status = ['Sprout', 'Green', 'Ready']
        self.status = self.growth_status[0]

    def __str__(self):
        return f'{self.num_potato}:{self.status}'


class Garden:

    def __init__(self, num_potato: int):
        self.num_potato = num_potato
        self.potato_list = []
        for i in range(num_potato):
            self.potato_list.append(Potato(i + 1))

    def grow(self):
        for i in self.potato_list:
            i.status = i.growth_status[i.growth_status.index(i.status) + 1]

    def print_potatoes(self):
        for i in self.potato_list:
            print(i)


class Gardener:

    def __init__(self, name: str, num_potato: int, looking_after: bool):
        self.gardener_name = name
        self.gardener_care = looking_after
        self.num = num_potato

    def look_after(self):
        if self.gardener_care:
            print('Gardener is looking after the crops.')
        else:
            print('Gardener is not looking after the crops')

    def collect(self):
        obj = Garden(5)
        obj.potato_list.clear()
        print(obj.potato_list)


garden = Garden(5)
gardener = Gardener('Vasya', 5, True)
garden.grow()
garden.print_potatoes()
garden.grow()
garden.print_potatoes()
gardener.look_after()
gardener.collect()
