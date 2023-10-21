class Node:
    def __init__(self):
        self.list = []

    def __str__(self) -> str:
        return f'Current list: {self.list}'

    def append(self, data):
        self.list.append(None)
        index = len(self.list) - 1
        while index > 0 and self.list[index - 1] is None:
            self.list[index] = self.list[index - 1]
            index -= 1

        self.list[index] = data

    def get(self, index):
        count = 0
        for element in self.list:
            if count == index:
                return element
            count += 1
        raise IndexError('Index out of range')

    def remove(self, index):
        for i in range(len(self.list)):
            if i == index:
                for j in range(i, len(self.list) - 1):
                    self.list[j] = self.list[j + 1]
                self.list.pop()
                return


class LinkedList(Node):
    def __init__(self):
        super().__init__()

    def __str__(self) -> str:
        return super().__str__()


mylist = LinkedList()
mylist.append(10)
mylist.append(20)
mylist.append(30)
print(mylist)
print(f'\nGetting the third element: {mylist.get(2)}\n')
print('Deleting the second element\n')
mylist.remove(1)
print(mylist)
