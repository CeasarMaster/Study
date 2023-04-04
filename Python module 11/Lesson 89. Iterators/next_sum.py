import random


class NextSum:

    def __init__(self, num_elements: int):
        self.num_elements = num_elements
        self.counter = 0
        self.first_element = round(random.uniform(0.0, 1.0), 2)
        self.current_num = 0
        self.next_num = round(random.uniform(0.0, 1.0), 2)

    def __iter__(self):
        self.counter = 0
        self.first_element = round(random.uniform(0.0, 1.0), 2)
        self.current_num = 0
        self.next_num = round(random.uniform(0.0, 1.0), 2)
        return self

    def __next__(self):
        self.counter += 1
        if self.counter > self.num_elements:
            raise StopIteration
        self.current_num, self.next_num = self.first_element, self.current_num + self.next_num
        return round(self.next_num, 2)


while True:
    n = int(input('Number of elements: '))
    x = NextSum(n)
    for i in x:
        print(i)
