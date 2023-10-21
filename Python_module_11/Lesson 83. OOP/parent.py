class Child:
    def __init__(self, name: str, age: int, calmness: bool, hunger: bool):
        self.child_name = name
        self.child_age = age
        self.calmness = calmness
        self.hunger = hunger

    def __str__(self):
        return f'Child:\n  Name: {self.child_name}\n  Age: {self.child_age}\n  Calmness: {self.calmness}\n  Hunger: {self.hunger}'


class Parent:
    def __init__(self, name: str, age: int, child: list):
        self.parent_name = name
        self.parent_age = age
        self.children_list = child

    def __str__(self):
        return f'Parent:\n  Name: {self.parent_name}\n  Age: {self.parent_age}\n  Children: {self.children_list}'

    def feed(self):
        for i in self.children_list:
            i.hunger = False

    def calm(self):
        for i in self.children_list:
            i.calmness = True


child = Child('Nikita', 15, False, True)
parent = Parent('Alexander', 56, [child])
print(parent)
print(child)
parent.calm()
print(child)
parent.feed()
print(child)
